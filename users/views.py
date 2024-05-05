import secrets

from django.contrib.auth import login
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.views import PasswordResetView
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.utils.http import urlsafe_base64_decode
from django.views import View
from django.views.generic import CreateView, UpdateView, TemplateView

from users.forms import UserRegisterForm, UserProfileForm
from users.models import User
from users.servises import activate_email_task, activate_new_password_task


class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        user: User = form.save()
        user.is_active = False
        user.save()
        activate_email_task(user)
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse_lazy("users:register_done")


class RegisterDoneView(TemplateView):
    template_name = "users/register_done.html"
    extra_context = {"title": "Регистрация завершена, активируйте учётную запись."}


class RegisterConfirmView(View):
    @staticmethod
    def get(request, uidb64, token):
        try:
            uid = urlsafe_base64_decode(uidb64)
            user = User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError):
            user = None
        if user is not None and default_token_generator.check_token(user, token):
            user.is_active = True
            user.save()
            login(request, user)
            return render(
                request,
                "users/register_confirmed.html",
                {"title": "Учётная запись активирована."},
            )
        else:
            return render(
                request,
                "users/register_not_confirmed.html",
                {"title": "Ошибка активации учётной записи."},
            )


class ProfileView(UpdateView):
    model = User
    form_class = UserProfileForm
    success_url = reverse_lazy('catalog:home')

    def get_object(self, queryset=None):
        return self.request.user


class UserPasswordResetView(PasswordResetView):
    form_class = PasswordResetForm
    template_name = 'users/password_reset_form.html'
    success_url = reverse_lazy('users:login')
    code = secrets.token_hex(8)

    def form_valid(self, form):
        if self.request.method == 'POST':
            email = self.request.POST['email']
            try:
                user = User.objects.filter(email=email).first()
                password = UserPasswordResetView.code
                user.set_password(password)
                user.save()
                activate_new_password_task(user, password)
                return HttpResponseRedirect(reverse('users:login'))
            except (Exception):
                return self.render_to_response('users:register')

        return super().form_valid(form)
