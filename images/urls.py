from django.urls import path
from .views import *

urlpatterns = [
    path('', home_view, name='home'),
    path('photography', home_view, name='photography'),
    path('birds', birds_view, name='birds'),
    path('waterfowls', waterfowls_view, name='waterfowls'),
    path('madison', madison_view, name='madison'),
    path('other', other_view, name='other'),
    path('paintings', paintings_view, name='paintings')
]