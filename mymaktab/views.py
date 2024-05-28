from django.shortcuts import render
from .forms import SearchSchoolForm

def search_school_view(request):
    if request.method == 'POST':
        form = SearchSchoolForm(request.POST)
        if form.is_valid():
            # Process the form data
            pass
    else:
        form = SearchSchoolForm()
    return render(request, 'index.html', {'form': form})
from django.http import JsonResponse
from .models import Region, Neighborhood, Street, House

def get_regions(request, oblast_id):
    regions = Region.objects.filter(oblast_id=oblast_id)
    return JsonResponse({'regions': [(r.id, r.name) for r in regions]})

def get_neighborhoods(request, region_id):
    neighborhoods = Neighborhood.objects.filter(region_id=region_id)
    return JsonResponse({'neighborhoods': [(n.id, n.name) for n in neighborhoods]})

def get_streets(request, neighborhood_id):
    streets = Street.objects.filter(neighborhood_id=neighborhood_id)
    return JsonResponse({'streets': [(s.id, s.name) for s in streets]})

def get_houses(request, street_id):
    houses = House.objects.filter(street_id=street_id)
    return JsonResponse({'houses': [(h.id, h.number) for h in houses]})
