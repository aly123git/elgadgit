from django.db import models

class toshiba(models.Model):
    power= models.CharField(max_length=50)
    warranty = models.CharField(max_length=10)
    price= models.CharField(max_length=10)
    image= models.ImageField(upload_to='toshiba_photo/')
    description= models.TextField(max_length=1000)

    def __str__(self):
        return self.power


class toshiba_ar(models.Model):
    power= models.CharField(max_length=50)
    warranty = models.CharField(max_length=10)
    price= models.CharField(max_length=10)
    image= models.ImageField(upload_to='toshiba_photo/')
    description= models.TextField(max_length=1000)

    def __str__(self):
        return self.power

