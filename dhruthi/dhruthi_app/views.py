from django.shortcuts import render
from .models import HomeSlider
# Create your views here.
def home(request):
    slider = HomeSlider.objects.all()
    return render( request,'uifiles/index.html',{'slider':slider})