# admin.py
from django.contrib import admin
from .models import SchoolAreaInfo, Houses, Coord

@admin.register(Coord)
class CoordAdmin(admin.ModelAdmin):
    list_display = ('lat', 'lng')

@admin.register(Houses)
class HousesAdmin(admin.ModelAdmin):
    list_display = ('cadastr_num', 'district', 'street_name', 'house_number')
    search_fields = ('cadastr_num', 'district', 'street_name', 'house_number')

@admin.register(SchoolAreaInfo)
class SchoolAreaInfoAdmin(admin.ModelAdmin):
    list_display = ('school_id', 'school_num', 'study_lang')
    search_fields = ('school_num',)
    filter_horizontal = ('houses',)
