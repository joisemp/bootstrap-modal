from django.db import models
from django.db.models.signals import pre_delete
from django.dispatch.dispatcher import receiver

class Picture(models.Model):
    item = models.ImageField(upload_to = 'images/')
    info = models.CharField(max_length=150)


    def __str__(self):
        return str(self.pk)

@receiver(pre_delete, sender=Picture)
def Post_delete(sender, instance, **kwargs):
    # Pass false so FileField doesn't save the model.
    instance.item.delete(False)
