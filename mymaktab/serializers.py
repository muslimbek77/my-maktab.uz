# serializers.py
from rest_framework import serializers
from .models import SchoolAreaInfo, Houses, Coord

class CoordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coord
        fields = ['lat', 'lng']

class HousesSerializer(serializers.ModelSerializer):
    coords = CoordSerializer()

    class Meta:
        model = Houses
        fields = ['cadastr_num', 'other_school_lang', 'erp_mahalla_id', 'erp_mahalla',
                  'address_uid', 'house_type', 'district_uid', 'district', 'district_soato',
                  'street_uid', 'street_name', 'house_number', 'object_type', 'coords']

class SchoolAreaInfoSerializer(serializers.ModelSerializer):
    houses = HousesSerializer(many=True)
    locations = CoordSerializer()

    class Meta:
        model = SchoolAreaInfo
        fields = ['school_id', 'school_num', 'study_lang', 'houses', 'locations']
