from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View

# Create your views here.

#def home(request):
#    return render(request, 'historyPay/HomePage.html', {})
class home(View):
    def get(self, request):
        #return HttpResponse('Result')
        return render(request, 'historyPay/HomePage.html', {})

class login(View):
    def get(self, request):
        return render(request, 'registrations/login.html', {})