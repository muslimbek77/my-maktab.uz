# models.py
from django.db import models

class Coord(models.Model):
    lat = models.DecimalField(max_digits=10, decimal_places=6)
    lng = models.DecimalField(max_digits=10, decimal_places=6)

    def __str__(self):
        return f"({self.lat}, {self.lng})"

class Houses(models.Model):
    cadastr_num = models.CharField(max_length=255)
    other_school_lang = models.CharField(max_length=255, blank=True)
    erp_mahalla_id = models.IntegerField(blank=True, null=True)
    erp_mahalla = models.CharField(max_length=255, blank=True)
    address_uid = models.CharField(max_length=255, blank=True)
    house_type = models.CharField(max_length=255, blank=True)
    district_uid = models.CharField(max_length=255, blank=True)
    district = models.CharField(max_length=255, blank=True)
    district_soato = models.CharField(max_length=255, blank=True)
    street_uid = models.CharField(max_length=255, blank=True)
    street_name = models.CharField(max_length=255, blank=True)
    house_number = models.CharField(max_length=255, blank=True)
    object_type = models.CharField(max_length=255, blank=True)
    coords = models.OneToOneField(Coord, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.cadastr_num} - {self.house_number}"

class SchoolAreaInfo(models.Model):
    school_id = models.IntegerField()
    school_num = models.CharField(max_length=255)
    study_lang = models.IntegerField()

    houses = models.ManyToManyField(Houses, blank=True)
    locations = models.OneToOneField(Coord, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"School {self.school_num}"
