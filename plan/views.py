from django.shortcuts import render

def home(request):
  
  return render(request, 'plan/index.html', {})

def planos(request):
  return render(request, 'plan/planos.html', {})

def sobre(request):
  return render(request, 'plan/sobre.html', {})