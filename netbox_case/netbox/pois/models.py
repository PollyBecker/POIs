from django.db import models

class POI(models.Model):
    name = models.CharField(max_length=100)
    x = models.PositiveIntegerField()
    y = models.PositiveIntegerField()
    description = models.CharField(max_length=300)

    def __str__(self):
        return self.name

