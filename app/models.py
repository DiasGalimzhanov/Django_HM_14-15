from django.db import models

class VideoCard(models.Model):
    class Manufacturer(models.TextChoices):
        MSI = 'MSI'
        GIGABYTE = 'GIGABYTE'
        INTEL = 'INTEL'
        NVIDIA = 'NVIDIA'
        AMD = 'AMD'

    name = models.CharField(max_length=100)
    memory = models.IntegerField()
    price = models.IntegerField()
    release_date = models.DateField()
    manufacturer = models.CharField(max_length=100, choices=Manufacturer.choices)

    def __str__(self):
        return self.name
    
