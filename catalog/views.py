from django import forms

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin, PermissionRequiredMixin
from django.forms import inlineformset_factory
from django.urls import reverse_lazy, reverse
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView

from catalog.forms import ProductForm, VersionForm, ProductModeratorForm
from catalog.models import Product, OurContact, Version


class IndexView(LoginRequiredMixin, TemplateView):
    template_name = 'catalog/product_list.html'
    extra_context = {'title': "Главная страница"}

    def get_context_data(self, **kwargs):
        filter_object_list = []
        context_data = super().get_context_data(**kwargs)
        context_data['object_list'] = Product.objects.filter(is_published=True).order_by("-id")[0:5]
        for product in context_data.get('object_list'):
            product.current_version = product.versions.filter(current_version=True).first()
            if product.current_version:
                filter_object_list.append(product)
        context_data['object_list'] = filter_object_list
        return context_data


class ProductCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("catalog:products")
    permission_required = 'catalog.add_product'
    raise_exeption = True

    def form_valid(self, form):
        if form.is_valid():
            product = form.save(commit=False)
            product.parent = self.request.user
            product.save()

        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):

    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("catalog:products")

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)

        VersionFormset = inlineformset_factory(Product, Version, form=VersionForm, extra=0)
        if self.request.method == 'POST':
            context_data['formset'] = VersionFormset(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = VersionFormset(instance=self.object)
        return context_data

    def form_valid(self, form):

        context = self.get_context_data()
        formset = context['formset']
        if form.is_valid():
            self.object = form.save()
            self.object.parent = self.request.user
        if formset.is_valid():
            formset.instance = self.object
            
            """ Проверка на наличие нескольких текущих (активных) версий товара"""
            count = 0
            for f in formset.forms:
                if f.cleaned_data['current_version']:
                    count += 1
            if count > 1:
                raise forms.ValidationError('Вы можете установить только одну версию в качестве текущей')

            formset.save()

        return super().form_valid(form)


class ProductUpdateModeratorView(ProductUpdateView):
    form_class = ProductModeratorForm


class ProductListView(LoginRequiredMixin, ListView):
    model = Product
    extra_context = {'title': "Товары"}
    permission_required = 'catalog.view_product'

    def get_context_data(self, **kwargs):
        # filter_object_list = []
        context_data = super().get_context_data(**kwargs)
        context_data['object_list'] = Product.objects.filter(is_published=True).order_by("-id")
        for product in context_data.get('object_list'):
            product.current_version = product.versions.filter(current_version=True).first()
            # if product.current_version:
            #     filter_object_list.append(product)
        context_data['set_published_status'] = self.request.user.groups.filter(name='product_moderator').exists()
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


class ProductDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Product
    extra_context = {'title': "Удаление товара"}
    success_url = reverse_lazy("catalog:products")

    def test_func(self):
        """Удалить товар может только superuser"""
        return self.request.user.is_superuser


class VersionListView(LoginRequiredMixin, ListView):
    model = Version
    extra_context = {'title': "Версии товара"}
    raise_exeption = True

    def get_queryset(self, *args, **kwargs):

        return Version.objects.filter(product=Product.objects.get(pk=self.kwargs.get('pk')))


class VersionCreateView(LoginRequiredMixin, CreateView):
    model = Version
    form_class = VersionForm
    success_url = reverse_lazy('catalog:products')
    extra_context = {'title': "Создание версии товара"}


class VersionUpdateView(LoginRequiredMixin, UpdateView):
    model = Version
    form_class = VersionForm
    success_url = reverse_lazy('catalog:products')
    extra_context = {'title': "Редактирование версии товара"}


class VersionDetailView(DetailView):
    model = Version
    context_object_name = 'versions'
    extra_context = {'title': "Версия товара"}


class VersionDeleteView(LoginRequiredMixin, DeleteView):
    model = Version
    success_url = reverse_lazy('catalog:products')
    extra_context = {'title': "Удаление версии товара"}
    raise_exeption = True

    def get_success_url(self):
        return reverse('catalog:products')
