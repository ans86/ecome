from django.urls import path
from . import views

urlpatterns = [
    path('category/<slug:category_slug>/', views.category_products, name='category_products'),
    path("product", views.product_list, name="product_list"),
    path("search/", views.search, name="search"),
    path('product/<slug:slug>/', views.product_detail, name='product_detail'),
    path('add/', views.add_product, name='add_product'),
    path("product/<slug:slug>/review/", views.add_review, name="add_review"),
    path('edit/<slug:slug>/', views.edit_product, name='edit_product'),
    path('delete/<slug:slug>/', views.delete_product, name='delete_product'),
    path('my_list/', views.my_list, name='my_list'),
    path('product/<slug:slug>/bid/', views.add_bid, name='add_bid'),
    path('product/<int:id>/edit-bid/', views.edit_bid, name='edit_bid'),
    path('products/<slug:slug>/close-bid/', views.close_bid, name='close_bid'),
    path("like/<slug:product_slug>/", views.add_like, name="add_like"),
    path('unlike/<slug:product_slug>/', views.unlike_product, name='unlike_product'),
    path("liked_products/", views.liked_products, name="liked_products"),
    path("cart/<slug:product_slug>/", views.add_cart, name="add_cart"),
    path("cart_products/", views.cart_products, name="cart_products"),



]
