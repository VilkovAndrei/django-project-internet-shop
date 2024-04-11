from django.urls import path
from catalog.views import ProductDetailView, IndexView, ProductListView, ProductCreateView, ContactsView, \
    ProductUpdateView, ProductDeleteView

app_name = 'catalog'


urlpatterns = [
    path('', IndexView.as_view(), name='home'),
    path('product_list/', ProductListView.as_view(), name='products'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('product_detail/<int:pk>', ProductDetailView.as_view(), name='product_detail'),
    path('product_create/', ProductCreateView.as_view(), name='product_create'),
    path('product_update/<int:pk>', ProductUpdateView.as_view(), name='product_update'),
    path('product_delete/<int:pk>', ProductDeleteView.as_view(), name='product_delete'),
]
