from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View, ListView
from .models import Period, ServiceProvider

class home(View):
    def get(self, request):        
        return render(request, 'historyPay/HomePage.html', {})

class login(View):
    def get(self, request):
        return render(request, 'registrations/login.html', {})

class serviceProviderList(View):
    def get(self, request):     
        provider = ServiceProvider.objects.all()
        provider = provider.extra(order_by=['name'])
        return render(request, 'historyPay/serviceProviderList.html', {'provider_list':provider})

class PeriodList(View):
    def get(self, request):        
        period = Period.objects.all()
        period = period.extra(order_by=['-begin_d'])
        return render(request, 'historyPay/PeriodList.html', {'period_list':period})
    
class PayList(View):
    def get(self, request):        
        return render(request, 'historyPay/PayList.html', {})
