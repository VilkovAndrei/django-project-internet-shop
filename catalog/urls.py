from django.urls import path
from django.views.decorators.cache import cache_page

from catalog.views import ProductDetailView, IndexView, ProductListView, ProductCreateView, ContactsView, \
    ProductUpdateView, ProductDeleteView, VersionListView, VersionCreateView, VersionUpdateView, VersionDetailView, \
    VersionDeleteView, ProductUpdateModeratorView, CategoryListView

app_name = 'catalog'


urlpatterns = [
    path('', IndexView.as_view(), name='home'),
    path('product_list/', cache_page(60)(ProductListView.as_view()), name='products'),
    path('category_list/', CategoryListView.as_view(), name='categories'),
    path('contacts/', cache_page(6000)(ContactsView.as_view()), name='contacts'),
    path('product_detail/<int:pk>', cache_page(60)(ProductDetailView.as_view()), name='product_detail'),
    path('product_create/', ProductCreateView.as_view(), name='product_create'),
    path('product_update/<int:pk>', ProductUpdateView.as_view(), name='product_update'),
    path('product_update_moderator/<int:pk>', ProductUpdateModeratorView.as_view(), name='product_update_moderator'),
    path('product_delete/<int:pk>', ProductDeleteView.as_view(), name='product_delete'),
    path('versions/<int:pk>', VersionListView.as_view(), name='versions'),
    path('version_create/', VersionCreateView.as_view(), name='version_create'),
    path('version_update/<int:pk>', VersionUpdateView.as_view(), name='version_update'),
    path('version_detail/<int:pk>', VersionDetailView.as_view(), name='version_detail'),
    path('version_delete/<int:pk>', VersionDeleteView.as_view(), name='version_delete'),
]
