from django.urls import path
from . import views


urlpatterns = [
    path('products/', views.add_product, name='add_product'),
]
