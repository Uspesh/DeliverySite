from django import template

register = template.Library()

@register.filter
def get_product_quantity(product, cart):
    return cart.get(str(product.pk), 0)

@register.filter
def total_element_price(product, cart):
    quantity = cart.get(str(product.pk), 0)
    price = product.price
    return quantity * price