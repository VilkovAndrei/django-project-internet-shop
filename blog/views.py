# from django.shortcuts import render
# from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, CreateView

from blog.models import Post


class PostListView(ListView):
    model = Post
    template_name = 'blog:post_list'
    extra_context = {'title': "Записи блога"}

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(is_published=True)
        return queryset
