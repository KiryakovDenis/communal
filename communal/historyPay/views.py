from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View

class home(View):
    def get(self, request):        
        return render(request, 'historyPay/HomePage.html', {})

class login(View):
    def get(self, request):
        return render(request, 'registrations/login.html', {})

class serviceProviderList(View):
    def get(self, request):        
        return render(request, 'historyPay/serviceProviderList.html', {})

class PeriodList(View):
    def get(self, request):        
        return render(request, 'historyPay/PeriodList.html', {})

class PayList(View):
    def get(self, request):        
        return render(request, 'historyPay/PayList.html', {})
