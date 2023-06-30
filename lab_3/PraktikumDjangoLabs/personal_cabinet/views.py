from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request): 
  return render(request, 'personal_cabinet/index.html', {'var': 'Some values of its variable.'})

def add(request):
  return render(request, 'personal_cabinet/add.html', {'var': 'It\'s a page of adding data.'})

def view(request):
  return render(request, 'personal_cabinet/view.html', {'var': 'It\'s a page of viewung data.'})
