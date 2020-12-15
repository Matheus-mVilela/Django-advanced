from django.shortcuts import render
from django.views import View


class DashBoard(View):
    def get(self, request):
        return render(request, 'vendas/dashboard.html')
