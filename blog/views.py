# from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from blog.models import Post
from blog.services import send_blog_email


class PostCreateView(CreateView):
    model = Post
    fields = ('title', 'description', 'preview', 'is_published')
    success_url = reverse_lazy("blog:post_list")
    extra_context = {'title': "Создание записи"}


class PostUpdateView(UpdateView):
    model = Post
    fields = ('title', 'description', 'preview', 'is_published')
    success_url = reverse_lazy("blog:post_list")
    extra_context = {'title': "Редактирование записи"}


class PostListView(ListView):
    model = Post
    template_name = 'blog:post_list'
    extra_context = {'title': "Записи блога"}

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(is_published=True).order_by("-id")
        return queryset


class PostDetailView(DetailView):
    model = Post
    extra_context = {'title': "Запись блога"}

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.count_view += 1
        if self.object.count_view == 20:
            send_blog_email(self.object)
        self.object.save()
        return self.object


class PostDeleteView(DeleteView):
    model = Post
    extra_context = {'title': "Удаление записи"}
