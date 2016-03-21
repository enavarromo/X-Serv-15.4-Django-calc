from django.shortcuts import render
from django.http import HttpResponse


def suma(request, num1, num2):
    return HttpResponse(num1+'+'+num2+'='+str(int(num1)+int(num2)))

def resta(request, num1, num2):
    return HttpResponse(num1+'-'+num2+'='+str(int(num1)-int(num2)))

def multiplica(request, num1, num2):
    return HttpResponse(num1+'*'+num2+'='+str(int(num1)*int(num2)))

def divide(request, num1, num2):
    return HttpResponse(num1+'/'+num2+'='+str(int(num1)/int(num2)))

def la404(request):
    return HttpResponse('Not Found')
