'''
Created on 29 mai 2016

@author: maelle
'''
from django.http import HttpResponse

def welcome(request):
    return HttpResponse("Hello, world.")