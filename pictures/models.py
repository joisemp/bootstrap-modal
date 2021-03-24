from django.db import models

class Picture(models.Model):
    item = models.ImageField(upload_to = 'images/')
    info = models.CharField(max_length=150)


    def __str__(self):
        return str(self.pk)
