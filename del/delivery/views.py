from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView
from .forms import UserInfo
from .models import Product, Menu


buttons = [
    {'title': 'Главная', 'url_name': 'main_page'},
    {'title': 'Меню', 'url_name': 'menu'},
    {'title': 'Акции', 'url_name': 'promotions'},
    {'title': 'Контакты', 'url_name': 'contacts'},
    {'title': 'Доставка и оплата', 'url_name': 'order'},
]

footer = [
    {'photo': 'delivery/img/footer-img 1.jpg'},
    {'photo': 'delivery/img/footer-img-2.jpg'},
    {'photo': 'delivery/img/footer-img-3.jpg'},
    {'photo': 'delivery/img/footer-img-4.jpg'},
    {'photo': 'delivery/img/footer-img-5.jpg'},
    {'photo': 'delivery/img/footer-img-6.jpg'},
    {'photo': 'delivery/img/footer-img-7.jpg'},
    {'photo': 'delivery/img/footer-img-8.jpg'},
]

def main_page(request):
    """генерация главной страницы"""
    data = Product.objects.all().filter(category_id = 1)
    title: str = 'Заказать комбо наборы в Краснодаре'
    cart = request.session.get('cart', {})
    products = Product.objects.filter(pk__in=cart.keys())
    total_price = sum(product.price * cart[str(product.pk)] for product in products)
    return render(request, 'delivery/main_page.html', {'data': data, 'buttons': buttons, 'title':title,
                                                       'cart': cart, 'total_price': total_price, 'footer': footer})

# меню и все что с ним связано

def menu(request):
    menu_data = Menu.objects.all()
    title: str = 'Меню'
    cart = request.session.get('cart', {})
    products = Product.objects.filter(pk__in=cart.keys())
    total_price = sum(product.price * cart[str(product.pk)] for product in products)
    return render(request, 'delivery/menu.html', {'buttons': buttons, 'menu_data': menu_data, 'title': title,
                                                  'cart': cart, 'total_price': total_price, 'footer': footer})

def element(request, element_slug):
    element = get_object_or_404(Product, slug=element_slug)
    title = element.title
    return render(request, 'delivery/base_el.html', {'element': element, 'title': title})

def combo(request):
    data = Product.objects.all().filter(category_id=1)
    title = 'Комбо наборы'
    cart = request.session.get('cart', {})
    products = Product.objects.filter(pk__in=cart.keys())
    total_price = sum([product.price * cart[str(product.pk)] for product in products])
    return render(request, 'delivery/menu/combo.html', {'data': data, 'buttons': buttons, 'title':title,
                                                        'cart': cart, 'total_price': total_price, 'footer': footer})

def sets(request):
    data = Product.objects.all().filter(category_id=2)
    title = 'Сеты'
    cart = request.session.get('cart', {})
    products = Product.objects.filter(pk__in=cart.keys())
    total_price = sum([product.price * cart[str(product.pk)] for product in products])
    return render(request, 'delivery/menu/sets.html', {'data': data, 'buttons': buttons, 'title':title,
                                                  'cart': cart, 'total_price': total_price, 'footer': footer})

def rolls(request):
    data = Product.objects.all().filter(category_id=3)
    title = 'Роллы'
    cart = request.session.get('cart', {})
    products = Product.objects.filter(pk__in=cart.keys())
    total_price = sum([product.price * cart[str(product.pk)] for product in products])
    return render(request, 'delivery/menu/rolls.html', {'data': data, 'buttons': buttons, 'title':title,
                                                  'cart': cart, 'total_price': total_price, 'footer': footer})


def baked_rolls(request):
    data = Product.objects.all().filter(category_id=4)
    title = 'Запеченные роллы'
    cart = request.session.get('cart', {})
    products = Product.objects.filter(pk__in=cart.keys())
    total_price = sum([product.price * cart[str(product.pk)] for product in products])
    return render(request, 'delivery/menu/baked_rolls.html', {'data': data, 'buttons': buttons, 'title':title,
                                                  'cart': cart, 'total_price': total_price, 'footer': footer})

def tempura(request):
    data = Product.objects.all().filter(category_id=5)
    title = 'Темпура'
    cart = request.session.get('cart', {})
    products = Product.objects.filter(pk__in=cart.keys())
    total_price = sum([product.price * cart[str(product.pk)] for product in products])
    return render(request, 'delivery/menu/tempura_el.html', {'data': data, 'buttons': buttons, 'title':title,
                                                  'cart': cart, 'total_price': total_price, 'footer': footer})


def pizza(request):
    data = Product.objects.all().filter(category_id=6)
    title = 'Пицца'
    cart = request.session.get('cart', {})
    products = Product.objects.filter(pk__in=cart.keys())
    total_price = sum([product.price * cart[str(product.pk)] for product in products])
    return render(request, 'delivery/menu/pizza.html', {'data': data, 'buttons': buttons, 'title':title,
                                                  'cart': cart, 'total_price': total_price, 'footer': footer})


def hot_snack(request):
    data = Product.objects.all().filter(category_id=7)
    title = 'Горячие закуски'
    cart = request.session.get('cart', {})
    products = Product.objects.filter(pk__in=cart.keys())
    total_price = sum([product.price * cart[str(product.pk)] for product in products])
    return render(request, 'delivery/menu/hot_snack.html', {'data': data, 'buttons': buttons, 'title':title,
                                                  'cart': cart, 'total_price': total_price, 'footer': footer})


def drinks(request):
    data = Product.objects.all().filter(category_id=8)
    title = 'Напитки'
    cart = request.session.get('cart', {})
    products = Product.objects.filter(pk__in=cart.keys())
    total_price = sum([product.price * cart[str(product.pk)] for product in products])
    return render(request, 'delivery/menu/drinks.html', {'data': data, 'buttons': buttons, 'title':title,
                                                  'cart': cart, 'total_price': total_price, 'footer': footer})


def optional(request):
    data = Product.objects.all().filter(category_id=9)
    title = 'Дополнительно'
    cart = request.session.get('cart', {})
    products = Product.objects.filter(pk__in=cart.keys())
    total_price = sum([product.price * cart[str(product.pk)] for product in products])
    return render(request, 'delivery/menu/optional.html', {'data': data, 'buttons': buttons, 'title':title,
                                                  'cart': cart, 'total_price': total_price, 'footer': footer})


def promotions(request):
    title = 'Акции'
    cart = request.session.get('cart', {})
    products = Product.objects.filter(pk__in=cart.keys())
    total_price = sum([product.price * cart[str(product.pk)] for product in products])
    return render(request, 'delivery/promotions.html', {'buttons': buttons, 'title': title,
                                                        'cart': cart, 'total_price': total_price, 'footer': footer})

def contacts(request):
    title = 'Контакты'
    cart = request.session.get('cart', {})
    products = Product.objects.filter(pk__in=cart.keys())
    total_price = sum([product.price * cart[str(product.pk)] for product in products])
    contact = '+7 (861) 250-69-79\n +7 (988) 240-20-58\n +7 (918) 975-99-16\n info@jackjackkrd.ru\n г. Краснодар, ул. 40-Летия Победы, д. 178к1\n г. Краснодар, ул. Минская, д. 46\n г. Краснодар, ул. Трамвайная, д. 1/1'
    ur_info = 'Фактический адрес: 350020, г. Краснодар, ул. Минская, д. 46\n\n Реквизиты:\n Юридический адрес: 350020, г. Краснодар, ул. Есенина, ул. 94\n ИП Цветкова Алена Сергеевна\n ОГРНИП 318237500213719 от 8 июня 2018 г.\n ИНН 910815552861'
    return render(request, 'delivery/contacts.html', {'buttons': buttons, 'title': title,
                                                      'contact': contact, 'ur_info': ur_info,
                                                      'cart': cart, 'total_price': total_price, 'footer': footer})

def order(request):
    title = 'Оплата и доставка заказов'
    cart = request.session.get('cart', {})
    products = Product.objects.filter(pk__in=cart.keys())
    total_price = sum([product.price * cart[str(product.pk)] for product in products])
    return render(request, 'delivery/order.html', {'buttons': buttons, 'title': title,
                                                   'cart': cart, 'total_price': total_price, 'footer': footer})

class GetInfo(CreateView):
    form_class = UserInfo
    template_name = 'delivery/get_info.html'
    success_url = ''
