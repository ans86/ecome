from django.urls import path
from . import views

urlpatterns = [
    path("product", views.product_list, name="product_list"),
    path("search/", views.search, name="search"),
    # urls.py
path("product/<int:id>/", views.product_detail, name="product_detail"),

    path('add/', views.add_product, name='add_product'),
    path("product/<int:id>/review/", views.add_review, name="add_review"),
    path('edit/<int:id>/', views.edit_product, name='edit_product'),
    path('delete/<int:id>/', views.delete_product, name='delete_product'),
    path('my_list/', views.my_list, name='my_list'),
    path('product/<int:id>/bid/', views.add_bid, name='add_bid'),
    path('product/<int:id>/edit-bid/', views.edit_bid, name='edit_bid'),
    path('products/<int:id>/close-bid/', views.close_bid, name='close_bid'),
    path("like/<int:product_id>/", views.add_like, name="add_like"),
    path('unlike/<int:product_id>/', views.unlike_product, name='unlike_product'),
    path("liked_products/", views.liked_products, name="liked_products"),


]
