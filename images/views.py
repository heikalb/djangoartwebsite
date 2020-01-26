from django.shortcuts import render
from .models import Image
# Create your views here.


def home_view(request):
    images = Image.objects.all()
    context = {'images': images}
    return render(request, 'images/image_list.html', context)