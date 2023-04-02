from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render, get_object_or_404
from django.views.decorators.http import require_POST

from cart.Cart import Cart
from cart.forms import CartAddProductForm
from delivery.forms import UserInfo
from delivery.models import Product
from delivery.views import buttons

quantity = 1
@require_POST
def cart_add(request, product_pk):
    cart = request.session.get('cart', {})
    cart[product_pk] = cart.get(product_pk, 0) + 1
    request.session['cart'] = cart
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    #return redirect('cart:cart_detail')

def cart_count(request, product_pk):
    cart = request.session.get('cart', {})
    if str(product_pk) in cart.keys():
        cart[str(product_pk)] += 1
        request.session['cart'] = cart
    return redirect('cart:cart_detail')

def cart_pop(request, product_pk):
    cart = request.session.get('cart', {})
    if str(product_pk) in cart.keys():
        cart[str(product_pk)] -= 1
        request.session['cart'] = cart
    if cart[str(product_pk)] < 1:
        cart_remove(request, product_pk)
        request.session['cart'] = cart
    return redirect('cart:cart_detail')

def cart_remove(request, product_pk):
    cart = request.session.get('cart', {})
    if str(product_pk) in cart.keys():
        del cart[str(product_pk)]
        request.session['cart'] = cart
    return redirect('cart:cart_detail')

def cart_detail(request):
    cart = request.session.get('cart', {})
    title = 'Корзина'
    form_class = UserInfo
    products = Product.objects.filter(pk__in=cart.keys())
    total_price = sum([product.price * cart[str(product.pk)] for product in products])
    return render(request, 'cart/detail1.html', {'cart': cart, 'products': products, 'total_price': total_price,
                                                'buttons': buttons, 'title': title, 'form': form_class})


# def cart_detail(request):
#     cart = request.session.get('cart', {})
#     products = Product.objects.filter(pk__in=cart.keys())
#     total_price = sum([product.price * cart[str(product.pk)]['quantity'] for product in products]) # Учитываем количество товара
#     return render(request, 'cart/detail.html', {'cart': cart, 'products': products, 'total_price': total_price})

# @require_POST
# def cart_add(request, product_pk):
#     cart = Cart(request)
#     product = get_object_or_404(Product, pk=product_pk)
#     form = CartAddProductForm(request.POST)
#     if form.is_valid():
#         cd = form.cleaned_data
#         cart.add(product=product, quantity=cd['quantity'],
#                  update_quantity=cd['update'])
#     return redirect('cart:cart_detail')
#
# def cart_remove(request, product_pk):
#     cart = Cart(request)
#     product = get_object_or_404(Product, pk=product_pk)
#     cart.remove(product)
#     return redirect('cart:cart_detail')
#
# def cart_detail(request):
#     cart = Cart(request)
#     print(cart)
#     return render(request, 'cart/detail1.html', {'cart': cart})