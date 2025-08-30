from django.urls import path
from . import views


urlpatterns = [
    path('laptops/', views.add_laptop, name='add_laptop'),
    path("laptop/<int:pk>/", views.laptop_detail, name="laptop_detail"),
    path("logout/", views.user_logout, name="logout"),
    path('form', views.car, name='car'),
]
