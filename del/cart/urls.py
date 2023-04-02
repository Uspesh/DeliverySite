from django.urls import path

from cart import views
from .views import *

app_name = 'cart'

urlpatterns = [
    path('', cart_detail, name = 'cart_detail'),
    path('add/<int:product_pk>/', cart_add, name='cart_add'), #<int:product_id>/
    path('count/<int:product_pk>/', cart_count, name='cart_count'), #<int:product_id>/
    path('pop/<int:product_pk>/', cart_pop, name='cart_pop'), #<int:product_id>/
    #path('quantity/<int:product_pk>/', get_product_quantity, name='get_product_quantity'), #<int:product_id>/
    path('remove/<int:product_pk>/', cart_remove, name='cart_remove')
]