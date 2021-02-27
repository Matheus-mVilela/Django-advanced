from django.urls import path
from vendas.views import DashBoard, CreateVendaView

urlpatterns = [
    path('dashboard/', DashBoard.as_view(), name='dashboard'),
    path('vendas/open/', CreateVendaView.as_view(), name='create-vendas'),
]
