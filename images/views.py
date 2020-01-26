from django.shortcuts import render
from .models import Image
# Create your views here.


def home_view(request):
    images = Image.objects.filter(featured=True)
    context = {'images': images}
    return render(request, 'images/image_list.html', context)


def list_view(request, category):
    images = Image.objects.filter(category=category).order_by('ranking')
    context = {'images': images}
    return render(request, 'images/image_list.html', context)


def birds_view(request):
    return list_view(request, 'Birds')


def waterfowls_view(request):
    return list_view(request, 'Waterfowls')


def madison_view(request):
    return list_view(request, 'Madison, WI')


def other_view(request):
    return list_view(request, 'Other')


def paintings_view(request):
    return list_view(request, 'Paintings')