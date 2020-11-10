from django.urls import path
from . import views


urlpatterns = [

        path('login/', views.login, name="login"),
        path('register/', views.register, name="register"), 
        path('logout/', views.logoutUser, name="logout"),

    path('', views.home, name="home"),
    #path('products/', views.products, name="products"),
    path('about/', views.about, name="about"),  
    path('customer/', views.customer, name="customer"),  
    path('vinyl/', views.vinyl, name="vinyl"),   
    path('laminate/', views.laminate, name="laminate"),  
    path('sales/', views.sales, name="sales"),  

    
]
