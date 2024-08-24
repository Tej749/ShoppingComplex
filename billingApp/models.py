from django.db import models

# Create your models here.

class Hotel(models.Model):
    name = models.CharField(max_length=50)
    loc = models.CharField(max_length=50)
    mob = models.CharField(max_length=10)
    email = models.EmailField()

    class Meta:
        db_table = 'hotel'

    def __str__(self):
        return self.name
