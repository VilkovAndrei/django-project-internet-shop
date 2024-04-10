from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, CreateView

from catalog.models import Product, OurContact


class IndexView(TemplateView):
    template_name = 'catalog/product_list.html'
    extra_context = {'title': "Главная страница"}

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['object_list'] = Product.objects.order_by("-id")[0:5]
        return context_data


class ProductCreateView(CreateView):
    model = Product
    fields = ('name', 'description', 'image', 'category', 'price')
    success_url = reverse_lazy("catalog:products")


class ProductListView(ListView):
    model = Product
    extra_context = {'title': "Товары"}
    paginate_by = 4

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['object_list'] = Product.objects.order_by("-id")
        context_data['paginate_by'] = 4
        return context_data


class ProductDetailView(DetailView):
    model = Product
    extra_context = {'title': "Товар"}


class ContactsView(TemplateView):
    model = OurContact
    template_name = 'catalog/contacts.html'
    extra_context = {'title': "Контакты"}

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['object'] = OurContact.objects.all()[0]
        return context_data
