from django.shortcuts import render
from .models import Image
# Create your views here.


def home_view(request):
    images = Image.objects.filter(featured=True).order_by('featured_ranking')

    description = "Photography from Madison, Wisconsin, USA, to Greater " \
                  "Vancouver, British Columbia, Canada. Fixated upon ducks, " \
                  "birds, pretty bugs, trees, leaves, water, reflections, winter " \
                  "and dusks."

    context = {'images': images, 'description': description}
    return render(request, 'images/image_list.html', context)


def list_view(request, category, description):
    images = Image.objects.filter(category=category).order_by('ranking')

    context = {'images': images, 'description': description}

    return render(request, 'images/image_list.html', context)


def birds_view(request):
    description = 'Birds, from House Sparrows to Sandhill Cranes.'
    return list_view(request, 'Birds', description)


def waterfowls_view(request):
    description = 'Birds, but on water.'
    return list_view(request, 'Waterfowls', description)


def madison_view(request):
    description = 'Sights from the city between two lakes.'
    return list_view(request, 'Madison, WI', description)


def other_view(request):
    description = 'Flora, insects, other places ...'
    return list_view(request, 'Other', description)


def paintings_view(request):
    description = 'Acrylic canvas paintings.'
    return list_view(request, 'Paintings', description)