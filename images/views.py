from django.shortcuts import render

# Create your views here.


def home_view(request):
    context = {}
    return request(request, 'images/image_list.html', context)