from django.urls import path
from . import views

urlpatterns=[
    path('',views.store,name="store"),
    path('cart/',views.cart,name="cart"),
    path('login/',views.login,name="login"),
    path('checkout/',views.checkout,name="checkout"),
    path('update_item/',views.updateItem,name="update_item"),
    path('process_order/',views.processOrder,name="process_order"),
]