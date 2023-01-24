from django.urls import path
from CHOCOLICA_WEB import views
urlpatterns=[
    path('',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('chocolate/',views.chocolate,name='chocolate'),
    path('discategorypage/<itemCatg>/',views.discategorypage,name='discategorypage'),
    path('singleproductpage/<int:dataid>/',views.singleproductpage,name='singleproductpage'),
    path('customerdetailspage/',views.customerdetailspage,name='customerdetailspage'),
    path('savecustomerdetails/',views.savecustomerdetails,name='savecustomerdetails'),
    path('customerloginpage/',views.customerloginpage,name='customerloginpage'),
    path('savecustomerlogin/',views.savecustomerlogin,name='savecustomerlogin'),
    path('logout/',views.logout,name='logout'),
    path('savecontact/',views.savecontact,name='savecontact'),
    path('Addtocart/',views.Addtocart,name='Addtocart'),
    path('cart/',views.showcart,name='showcart'),


]