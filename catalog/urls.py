from django.urls import path
from catalog.views import home

app_name = 'catalog'

urlpatterns = [
    path('', home, name='home'),
]