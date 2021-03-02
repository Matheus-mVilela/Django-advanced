from django.urls import path
from vendas.views import DashBoard, CreateVendaView, api

urlpatterns = [
    path('dashboard/', DashBoard.as_view(), name='dashboard'),
    path('open/', CreateVendaView.as_view(), name='create-vendas'),
     path('api/', api, name='api'),
]
