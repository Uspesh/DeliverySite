from django.urls import path

from cart import views
from cart.views import cart_detail
from .views import *

urlpatterns = [
    path('', main_page, name = 'main_page'),
    path('menu/', menu, name='menu'),
    path('menu/combo/', combo, name='combo'),
    path('element/<slug:element_slug>/', element, name='element'),
    path('menu/sets/', sets, name='sets'),
    path('menu/rolls/', rolls, name='rolls'),
    path('menu/baked_rolls/', baked_rolls, name='baked_rolls'),
    path('menu/tempura/', tempura, name='tempura'),
    path('menu/pizza/', pizza, name='pizza'),
    path('menu/hot_snack', hot_snack, name='hot_snack'),
    path('menu/drinks/', drinks, name='drinks'),
    path('menu/optional/', optional, name='optional'),
    path('promotions/', promotions, name='promotions'),
    path('contacts/', contacts, name='contacts'),
    path('order/', order, name='order'),
    #path('cart/order/', UserInfo.as_view(), name = 'get_info')
]