from django.db import models

# Create your models here.
class HomeSlider(models.Model):
        Id = models.IntegerField(primary_key = True)
        Title = models.CharField(max_length=25,default="heading")
        Image = models.ImageField(upload_to='uploads/')
        def __str__(self):
            return self.Title

class Popup(models.Model):
        Id = models.IntegerField(primary_key = True)
        Title = models.CharField(max_length=25,default="heading")
        Image = models.ImageField(upload_to='uploads/')
        def __str__(self):
            return self.Title