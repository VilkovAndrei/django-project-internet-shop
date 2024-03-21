from django.shortcuts import render

def home(request):
    return render(request, 'catalog/home.html', {'title':"Главная страница"})

def contacts(request):
    if request.method == 'POST':
        # в переменной request хранится информация о методе, который отправлял пользователь
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        # а также передается информация, которую заполнил пользователь
        print(name, phone, message)
    return render(request, 'catalog/contacts.html', {'title':"Контакты"})
