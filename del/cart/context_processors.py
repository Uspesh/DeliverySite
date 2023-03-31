from cart.Cart import Cart


def cart(request):
    return {'cart': Cart(request)}