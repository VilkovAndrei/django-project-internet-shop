from django.urls import path
from catalog.views import contacts, product_item, IndexView, ProductListView

app_name = 'catalog'

urlpatterns = [
    path('', IndexView.as_view(), name='home'),
    path('product_list/', ProductListView.as_view(), name='products'),
    path('contacts/', contacts, name='contacts'),
    path('product_item/<int:pk>', product_item, name='product_item')
]
