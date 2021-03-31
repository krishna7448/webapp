from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
import psutil, os
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def home(request):
    data = {
        'title' : "Dashboard"
    }
    return render(request, "backend/index.html", context=data)
