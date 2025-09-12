from django.urls import path
from . import views

urlpatterns = [
    path("product", views.product_list, name="product_list"),
    path("product/<int:id>/", views.product_detail, name="product_detail"),
    path('add/', views.add_product, name='add_product'),
    path("product/<int:id>/review/", views.add_review, name="add_review"),
    path('edit/<int:id>/', views.edit_product, name='edit_product'),
    path('delete/<int:id>/', views.delete_product, name='delete_product'),
    path('my_list/', views.my_list, name='my_list'),

]
