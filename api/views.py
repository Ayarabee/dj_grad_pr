from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import *
from .serializers import *
from rest_framework import status
from rest_framework.response import Response

import tensorflow as tf
import numpy as np


# Create your views here.


# Model Initialization
respiratory_model = tf.keras.models.load_model('Respiratory Model.h5')
print("Model Initialized!")


class RespiratoryDetectionViewSet(ModelViewSet):
    queryset = RespiratoryDetection.objects.all()
    serializer_class = RespiratoryDetectionSerializer

    def perform_create(self, serializer):
        result = serializer.save()

        image_url = serializer.instance.image.path
        detection_result = self.detection(image_url)
        if detection_result == 1:
            result.result = "Pneumonia Detected"
            result.result_class = 1
        else:
            result.result = "No Pneumonia Detected"
            result.result_class = 0

        result.save()

    def detection(self, imageUrl, *args, **kwargs):
        img = tf.keras.preprocessing.image.load_img(imageUrl, target_size=(150, 150))
        img_array = tf.keras.preprocessing.image.img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0)
        img_array = img_array / 255.0

        prediction = respiratory_model.predict(img_array)
        class_index = np.argmax(prediction)

        return class_index






