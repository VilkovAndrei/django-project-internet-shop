# from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from pytils.translit import slugify

from blog.models import Post
from blog.services import send_blog_email


class PostCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = 'blog.add_post'
    model = Post
    fields = ('title', 'description', 'preview', 'is_published')
    success_url = reverse_lazy("blog:post_list")
    extra_context = {'title': "Создание записи блога"}

    # def get_success_url(self):
    #     return reverse_lazy('blog:post_detail', kwargs={'pk': self.object.pk})

    # def form_valid(self, form):
    #     if form.is_valid():
    #         new_post = form.save()
    #         new_post.slug = slugify(self.title)
    #         new_post.save()
    #
    #     return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UpdateView):
    permission_required = 'blog.change_post'
    model = Post
    fields = ('title', 'description', 'preview', 'is_published')
    extra_context = {'title': "Редактирование записи блога"}

    def get_success_url(self):
        return reverse_lazy('blog:post_detail', kwargs={'pk': self.object.pk})


class PostListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'blog:post_list'
    extra_context = {'title': "Записи блога"}

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(is_published=True).order_by("-id")
        return queryset


class PostDetailView(LoginRequiredMixin, DetailView):
    permission_required = 'blog.view_post'
    model = Post
    extra_context = {'title': "Запись блога"}

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.count_view += 1
        if self.object.count_view == 100:
            send_blog_email(self.object)
        self.object.save()
        return self.object


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    permission_required = 'blog.delete_post'
    model = Post
    extra_context = {'title': "Удаление записи блога"}

    def test_func(self):
        """Удалить post может только superuser"""
        return self.request.user.is_superuser
