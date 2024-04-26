from django.urls import path
from catalog.views import ProductDetailView, IndexView, ProductListView, ProductCreateView, ContactsView, \
    ProductUpdateView, ProductDeleteView, VersionListView, VersionCreateView, VersionUpdateView, VersionDetailView, \
    VersionDeleteView

app_name = 'catalog'


urlpatterns = [
    path('', IndexView.as_view(), name='home'),
    path('product_list/', ProductListView.as_view(), name='products'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('product_detail/<int:pk>', ProductDetailView.as_view(), name='product_detail'),
    path('product_create/', ProductCreateView.as_view(), name='product_create'),
    path('product_update/<int:pk>', ProductUpdateView.as_view(), name='product_update'),
    path('product_delete/<int:pk>', ProductDeleteView.as_view(), name='product_delete'),
    path('versions/<int:pk>', VersionListView.as_view(), name='versions'),
    path('version_create/', VersionCreateView.as_view(), name='version_create'),
    path('version_update/<int:pk>', VersionUpdateView.as_view(), name='version_update'),
    path('version_detail/<int:pk>', VersionDetailView.as_view(), name='version_detail'),
    path('version_delete/<int:pk>', VersionDeleteView.as_view(), name='version_delete'),
]
