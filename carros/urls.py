from django.urls import path
from . import views

urlpatterns = [
    path('carros/', views.listar_carros),
    path('carros/disponiveis', views.listar_carros_disponiveis),
    path('carros/reservados', views.listar_carros_reservados),
    path('carros/vendidos', views.listar_carros_vendidos),
]