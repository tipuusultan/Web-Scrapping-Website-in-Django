from django.shortcuts import render, redirect
import requests
from bs4 import BeautifulSoup

# Create your views here.

def index(request):
    return render(request, 'index.html')

def result(request):
    url = request.GET.get('url')
    if url == "":
        return redirect(request, 'index.html')

    else:
        url = request.GET.get('url')
        r = requests.get(url)
        content = r.content
        soup = BeautifulSoup(content , 'html.parser')
        context = {
            "result": soup 
        }
        return render(request, 'index.html', context)
  

def theme(request):
    return render(request, 'bootstraptheme.html')