from django.urls import path
from myapp import views

urlpatterns = [
    #path('coupon/', views.Coupon_n.as_view()),
    path('coupon/<int:pk>/', views.Coupon1.as_view()),
    
]