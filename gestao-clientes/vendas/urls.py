from django.urls import path
from vendas.views import DashBoard, Vendas

urlpatterns = [
    path('dashboard/', DashBoard.as_view(), name='dashboard'),
    path('venda/', Vendas.as_view(), name='venda'),
]
