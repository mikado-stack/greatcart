from django.urls import path
from . import views

urlpatterns = [
    path('place_order/', views.place_order, name='place_order'),
    path('payments/', views.payments, name='payments'),
    path('order_complete/', views.order_complete, name='order_complete'),
    
    path('initiate-payment/', views.initiate_payment, name='initiate_payment'),
	path('verify-payment/<str:ref>/', views.verify_payment, name='verify_payment'),
]
