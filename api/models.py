from django.db import models

# Create your models here.
class Cancer(models.Model):
    key = models.CharField(max_length=200)
    value = models.CharField(max_length=200)

    def __str__(self):
        return self.key
    
