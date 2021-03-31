from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.forms.utils import ErrorList
from django.http import HttpResponse, JsonResponse
from .forms import signForm
import psutil, os, random

# Create your views here.

def home(request):
    return render(request, "frontend/index.html")

def about(request):
    characters = list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!#$%&()*+,-./:;<=>?@[]^_`{|}~')
    newpassword = ""
    
    for x in range(20):
        newpassword += random.choice(characters)

    data ={
        'newpassword':newpassword
    }
    return render(request, "frontend/about.html", context=data)
def serverStatus(request):
    
    return render(request, "frontend/serverstatus.html")
    

def getSeratusData(request):
    percent_sign = '%'
    mbsign = 'MB'
    cpu = psutil.cpu_percent()
    vram = psutil.virtual_memory()
    
    ram_total = vram[0]/ (1024 * 1024)
    ram_available = vram[1]/ (1024 * 1024)
    ram_percent = vram[2]
    ram_used = vram[3]/ (1024 * 1024)
    ram_free = vram[4]/ (1024 * 1024)
    totaldiskdevice = psutil.disk_partitions()
    diskmount = []
#    i = 1
    for x in totaldiskdevice:
        diskmount.append(psutil.disk_usage(x[1]))
        print(x[1])
        
 #   disk = []
    
    

    print(psutil.disk_usage(x[1]))
#    print(psutil.disk_io_counters(perdisk=False))


    #print(vram)
    data = {
        'cpu' : str(cpu)  + str(percent_sign),
        'ram_total' : str(round(ram_total)) + mbsign,
        'ram_available' : str(round(ram_available)) + mbsign,
        'ram_percent' : str(ram_percent) + percent_sign,
        'ram_used' : str(round(ram_used)) + mbsign,
        'ram_free' : str(round(ram_free)) + mbsign,
        'disk' : diskmount
        
    }
    return JsonResponse(data)
def userProfile(request):
    if request.user.is_authenticated:
        #User.objects.all()
        userdata = User.objects.get(username = request.user.get_username())
        data = {
            'userdata' : userdata
        }
        return render(request, "frontend/userProfile.html", context=data)
    else:
        return redirect("/login/")


def userLogout(request):
    logout(request)
    return redirect("/login/")

def userSign(request):
    if not request.user.is_authenticated:
        msg = None
        form = signForm(request.POST or None)
        if request.method == "POST":
            if form.is_valid():
                username = request.POST['username']
                password = request.POST['password']
                user = authenticate(request, username=username, password=password)
                print(user)
                if user is not None:
                    login(request, user)
                    return redirect("/")
                else:
                    msg = 'Invalid credentials'
            else:
                msg = 'Error validating the form'
            
        signform = signForm()
        data = {
            'signform' : signform,
            'msg' : msg
        }
        return render(request, "frontend/login.html", context=data)

    else:
        return redirect('/admin/')