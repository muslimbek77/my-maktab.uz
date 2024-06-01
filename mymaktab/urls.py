# urls.py
from django.urls import path
from .views import SchoolFinderAPIView

urlpatterns = [
    path('api/school-finder/', SchoolFinderAPIView.as_view(), name='school-finder'),
]
