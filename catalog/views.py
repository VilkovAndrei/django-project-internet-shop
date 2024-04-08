from django.shortcuts import render
from django.views.generic import TemplateView, ListView

from catalog.models import Product, OurContact


class IndexView(TemplateView):
    template_name = 'catalog/home.html'
    extra_context = {'title': "Главная страница"}

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['object_list'] = Product.objects.order_by("-id")[0:5]
        return context_data


class ProductListView(ListView):
    model = Product
    extra_context = {'title': "Товары"}

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['object_list'] = Product.objects.order_by("-id")
        return context_data

# def home(request):
#     return render(request, 'catalog/home.html', {'title': "Главная страница",
#                   'object_list': Product.objects.order_by("-id")[0:5]})


def contacts(request):
    if request.method == 'POST':
        # в переменной request хранится информация о методе, который отправлял пользователь
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        # а также передается информация, которую заполнил пользователь

    return render(request, 'catalog/contacts.html', {'title': "Контакты", 'object': OurContact.objects.first()})


def product_item(request, pk):
    return render(request, 'catalog/product_item.html', {'title': "Товар",
                  'object': Product.objects.get(pk=pk)})
