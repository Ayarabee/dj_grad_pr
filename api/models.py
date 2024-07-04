from django.db import models

# Create your models here.



class RespiratoryDetection(models.Model):
    image = models.ImageField(upload_to='respiratory')
    result_class = models.IntegerField(blank=True, null=True, editable=False)
    result = models.CharField(max_length=255, blank=True, null=True, editable=False)
    doctor_id = models.IntegerField()