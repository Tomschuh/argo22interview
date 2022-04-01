from distutils.command.upload import upload
from django.db import models

class QRDocument(models.Model):
    expiration_date = models.DateField(blank=True, null=True)
    # image = models.ImageField(upload_to="./images/", blank=False)
    imageBase64 = models.TextField(blank=False, null=False, default='')
    
    class ProcessState(models.TextChoices):
        PENDING = "PENDING"
        EXPIRED = "EXPIRED"
        VALID = "VALID"
        FRAUD = "FRAUD"
    process_state = models.CharField(max_length=10, choices=ProcessState.choices, default=ProcessState.PENDING)
    
    
    
    