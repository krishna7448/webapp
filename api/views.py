from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
import psutil, os
from django.contrib.auth import authenticate, login, logout
from pyami_asterisk import AMIClient

from . import asterisk
#from asterisk.ami import AMIClient, AMIClientAdapter, SimpleAction, EventListener
# Create your views here.

def apitest(request):
    data = {
        'name' : 'testapi',
        'method' : request.method
    }
    return JsonResponse(data)




def test_asterisk(request):
    asterisk.main()
    return HttpResponse()
