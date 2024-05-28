# from django.db import models

# # Create your models here.
# class School(models.Model):
#     LANG = {
#     "UZ": "O'zbek tili",
#     "RU": "Rus tili",
#     "TJK": "Tojik tili",
#     "QZ": "Qozoq tili",
# }
#     district = models.CharField(max_length=200)
#     school = models.CharField(max_length=200)
#     main_language = models.CharField(max_length=50,choices=LANG,default="UZ")
#     school_power = models.PositiveIntegerField()
#     students_count = models.PositiveIntegerField()
#     coefficient = models.FloatField()
from django.db import models

class Oblast(models.Model):
    name = models.CharField(max_length=100)

class Region(models.Model):
    name = models.CharField(max_length=100)
    oblast = models.ForeignKey(Oblast, on_delete=models.CASCADE)

class Neighborhood(models.Model):
    name = models.CharField(max_length=100)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)

class Street(models.Model):
    name = models.CharField(max_length=100)
    neighborhood = models.ForeignKey(Neighborhood, on_delete=models.CASCADE)

class House(models.Model):
    number = models.CharField(max_length=10)
    street = models.ForeignKey(Street, on_delete=models.CASCADE)

class LanguageEducation(models.Model):
    name = models.CharField(max_length=100)
