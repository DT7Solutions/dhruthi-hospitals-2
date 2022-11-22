from django.shortcuts import render
from .models import HomeSlider
# Create your views here.
def home(request):
    slider = HomeSlider.objects.all()
    return render( request,'uifiles/index.html',{'slider':slider})

def page_not_found_view(request, exception):
    return render(request, 'uifiles/404.html', status=404)