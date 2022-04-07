from django.db import models
from django.contrib.gis.db import models

class HealthFacilities(models.Model):
    geom = models.PointField(blank=True, null=True)
    addr_city = models.CharField(max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    addr_street = models.CharField(max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    name = models.CharField(max_length=255, blank=True, null=True)
    contact_phone = models.CharField(max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.

    # class Meta:
    #     managed = False
    #     db_table = 'health_facilities'

class SubCounties(models.Model):
    geom = models.MultiPolygonField(blank=True, null=True)
    constituent = models.CharField(max_length=50, blank=True, null=True)

    # class Meta:
    #     managed = False
    #     db_table = 'sub_counties'