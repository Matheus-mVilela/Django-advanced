from django.urls import path
from vendas.views import DashBoard

urlpatterns = [
    path('dashboard/', DashBoard.as_view(), name='dashboard'),
]
