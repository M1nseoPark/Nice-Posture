from django.db import models

# Create your models here.
class Park(models.Model):
    id = models.CharField(primary_key=True, max_length=10)
    name = models.CharField(max_length=50, blank=True, null=True)
    address = models.CharField(max_length=500, blank=True, null=True)
    latitude = models.CharField(max_length=50, blank=True, null=True)
    longitude = models.CharField(max_length=50, blank=True, null=True)
    image = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'park'
