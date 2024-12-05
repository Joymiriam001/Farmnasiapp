from django.urls import path
from . import views

urlpatterns=[
    path('',views.home,name='my_home'),
    path('seasons/',views.seasons,name='seasons'),
    path('product/',views.product, name='product'),
    path('cereals/', views.cereals, name='cereals'),
    path('beverage/', views.beverage, name='beverage'),
    path('fruits/', views.fruits, name='fruits'),
    path('vegetables/', views.vegetables, name='vegetables'),
    path('legumes/', views.legumes, name='legumes'),
    path('contact/', views.legumes, name='contact'),



]