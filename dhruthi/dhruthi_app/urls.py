
from django.urls import path
from .views import home,Chirala,Harikrishna
urlpatterns = [
    path('', home, name='home'),
    path('chirala/', Chirala, name='chirala'),
    path('RevuriHarikrishna/', Harikrishna, name='RevuriHarikrishna'),
]
