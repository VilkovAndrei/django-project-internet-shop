from django.shortcuts import render

from catalog.models import Product, OurContact


def home(request):
    return render(request, 'catalog/home.html', {'title': "Главная страница",
                  'object_list': Product.objects.order_by("-id")})


def contacts(request):
    if request.method == 'POST':
        # в переменной request хранится информация о методе, который отправлял пользователь
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        # а также передается информация, которую заполнил пользователь
        print(name, phone, message)
    return render(request, 'catalog/contacts.html', {'title': "Контакты", 'object': OurContact.objects.first()})


def product_item(request, pk):
    return render(request, 'catalog/product_item.html', {'title': "Товар",
                  'object': Product.objects.get(pk=pk)})
