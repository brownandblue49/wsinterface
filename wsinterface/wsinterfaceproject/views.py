from django.shortcuts import render
import requests
from subprocess import run,PIPE
import sys

# Create your views here.

def button(request):
    return render(request , 'wsinterfaceproject/home.html')

def output(request):
    data = requests.get("https://reqres.in/api/users")    
    print(data.text)
    data = data.text
    return render(request , 'wsinterfaceproject/home.html' , {'data' : data})

def external(request):
    inp = request.POST.get('fileupload') 
    run([sys.executable , 'BreakSingleVideotoFrames.py', inp] ,shell=False ,stdout = PIPE) 
   # out = "file submitted Successfully"
    return render(request , 'wsinterfaceproject/home.html' )

