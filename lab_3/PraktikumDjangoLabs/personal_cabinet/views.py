from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
  return render(request, 'personal_cabinet/index.html', {'var': 'Some values of its variable.'})
