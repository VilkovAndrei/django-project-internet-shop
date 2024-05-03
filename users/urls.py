from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from users.views import RegisterView, ProfileView, RegisterDoneView, RegisterConfirmView

app_name = 'users'


urlpatterns = [
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('register_done/', RegisterDoneView.as_view(), name='register_done'),
    path('register_confirmed/<uidb64>/<token>/', RegisterConfirmView.as_view(), name="register_confirmed"),
    # path('register_not_confirmed/', RegisterConfirmView.as_view(), name="register_not_confirmed"),

    path('profile/', ProfileView.as_view(), name='profile'),
]