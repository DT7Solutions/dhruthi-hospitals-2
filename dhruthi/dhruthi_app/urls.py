
from django.urls import path
from .views import home,Chirala
urlpatterns = [
    path('', home, name='home'),
    path('chirala/', Chirala, name='chirala'),
]
