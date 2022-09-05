from django.db import models

# Create your models here.
class whatsappdb(models.Model):
    name = models.CharField(max_length=200)
    contact = models.IntegerField()
    photo = models.ImageField(upload_to='images/',default="")
    pdf = models.FileField(upload_to='docs/')