from django.urls import path
from catalog.views import home, contacts, product_item

app_name = 'catalog'

urlpatterns = [
    path('', home, name='home'),
    path('contacts/', contacts, name='contacts'),
    path('product_item/<int:pk>', product_item, name='product_item')
]
