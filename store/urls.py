
from django.urls import path
from .views import Index , signup , Login , logout , Cart , CheckOut , OrderView
from .middlewares.auth import auth_middleware


urlpatterns = [
    path('', Index.as_view() , name='homepage'),
    path('signup', signup , name='signup'),
    path('login' , Login.as_view() , name='login'),
    path('logout', logout , name='logout'),
    path('cart', Cart.as_view() , name='cart'),
    path('check-out', CheckOut.as_view() , name='checkout'),
     path('orders', auth_middleware(OrderView.as_view()) , name='orders')
]