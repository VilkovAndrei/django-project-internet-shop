from django.db import transaction
from django.forms import inlineformset_factory
from django.urls import reverse_lazy, reverse
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView

from catalog.forms import ProductForm, VersionForm
from catalog.models import Product, OurContact, Version


class IndexView(TemplateView):
    template_name = 'catalog/product_list.html'
    extra_context = {'title': "Главная страница"}

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['object_list'] = Product.objects.order_by("-id")[0:5]
        return context_data


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("catalog:products")


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("catalog:products")

    def get_success_url(self, *args, **kwargs):
        return reverse('catalog:product_update', args=[self.get_object().pk])

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        VersionFormset = inlineformset_factory(Product, Version, form=VersionForm, extra=0)
        if self.request.method == 'POST':
            context_data['formset'] = VersionFormset(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = VersionFormset(instance=self.object)
        return context_data

    def form_valid(self, form):
        formset = self.get_context_data()['formset']
        self.object = form.save()
        if formset.is_valid():
            formset.instance = self.object
            form.save()

        return super().form_valid(form)


class ProductListView(ListView):
    model = Product
    extra_context = {'title': "Товары"}
    paginate_by = 4

    def get_context_data(self, **kwargs):
        filter_object_list = []
        context_data = super().get_context_data(**kwargs)
        context_data['object_list'] = Product.objects.order_by("-id")
        for product in context_data.get('object_list'):
            product.current_version = product.versions.filter(current_version=True).first()
            if product.current_version:
                filter_object_list.append(product)
        context_data['object_list'] = filter_object_list
        # context_data['paginate_by'] = 4
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


class ProductDeleteView(DeleteView):
    model = Product
    extra_context = {'title': "Удаление товара"}


class VersionListView(ListView):
    model = Version
    extra_context = {'title': "Версии товара"}

    def get_queryset(self, *args, **kwargs):

        return Version.objects.filter(product=Product.objects.get(pk=self.kwargs.get('pk')))


class VersionCreateView(CreateView):
    model = Version
    form_class = VersionForm
    success_url = reverse_lazy('catalog:products')
    extra_context = {'title': "Создание версии товара"}


class VersionUpdateView(UpdateView):
    model = Version
    form_class = VersionForm
    success_url = reverse_lazy('catalog:products')
    extra_context = {'title': "Редактирование версии товара"}


class VersionDetailView(DetailView):
    model = Version
    context_object_name = 'versions'
    extra_context = {'title': "Версия товара"}


class VersionDeleteView(DeleteView):
    model = Version
    success_url = reverse_lazy('catalog:versions')
