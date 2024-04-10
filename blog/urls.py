from django.urls import path

from blog.views import PostListView

app_name = 'blog'


urlpatterns = [
    # path('', IndexView.as_view(), name='home'),
    path('post_list/', PostListView.as_view(), name='post_list'),
    # path('contacts/', ContactsView.as_view(), name='contacts'),
    # path('product_detail/<int:pk>', ProductDetailView.as_view(), name='product_detail'),
    # path('product_create/', ProductCreateView.as_view(), name='product_create'),
]