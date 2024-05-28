from django.urls import path
from . import views

urlpatterns = [
    path('', views.search_school_view, name='search_school'),
    path('ajax/get_regions/<int:oblast_id>/', views.get_regions, name='get_regions'),
    path('ajax/get_neighborhoods/<int:region_id>/', views.get_neighborhoods, name='get_neighborhoods'),
    path('ajax/get_streets/<int:neighborhood_id>/', views.get_streets, name='get_streets'),
    path('ajax/get_houses/<int:street_id>/', views.get_houses, name='get_houses'),
]
