# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import SchoolAreaInfo, Houses
from .serializers import SchoolAreaInfoSerializer

class SchoolFinderAPIView(APIView):

    def get(self, request, *args, **kwargs):
        district = request.query_params.get('district')
        erp_neighbourhood = request.query_params.get('erp_neighbourhood')
        street_name = request.query_params.get('street_name')
        house_number = request.query_params.get('house_number')
        other_school_lang = request.query_params.get('other_school_lang')

        houses = Houses.objects.filter(
            district=district,
            erp_mahalla=erp_neighbourhood,
            street_name=street_name,
            house_number=house_number,
            other_school_lang=other_school_lang
        )
        # print(district)

        if houses.exists():
            school_area_info = SchoolAreaInfo.objects.filter(houses__in=houses).distinct()
            serializer = SchoolAreaInfoSerializer(school_area_info, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response({"message": "No matching schools found"}, status=status.HTTP_404_NOT_FOUND)
