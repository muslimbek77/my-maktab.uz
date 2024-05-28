from django.contrib import admin
from .models import Oblast, Region, Neighborhood, Street, House, LanguageEducation

class RegionInline(admin.TabularInline):
    model = Region
    extra = 1

class NeighborhoodInline(admin.TabularInline):
    model = Neighborhood
    extra = 1

class StreetInline(admin.TabularInline):
    model = Street
    extra = 1

class HouseInline(admin.TabularInline):
    model = House
    extra = 1

@admin.register(Oblast)
class OblastAdmin(admin.ModelAdmin):
    list_display = ('name',)
    inlines = [RegionInline]

@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = ('name', 'oblast')
    list_filter = ('oblast',)
    search_fields = ('name',)
    inlines = [NeighborhoodInline]

@admin.register(Neighborhood)
class NeighborhoodAdmin(admin.ModelAdmin):
    list_display = ('name', 'region')
    list_filter = ('region',)
    search_fields = ('name',)
    inlines = [StreetInline]

@admin.register(Street)
class StreetAdmin(admin.ModelAdmin):
    list_display = ('name', 'neighborhood')
    list_filter = ('neighborhood',)
    search_fields = ('name',)
    inlines = [HouseInline]

@admin.register(House)
class HouseAdmin(admin.ModelAdmin):
    list_display = ('number', 'street')
    list_filter = ('street',)
    search_fields = ('number',)

@admin.register(LanguageEducation)
class LanguageEducationAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
