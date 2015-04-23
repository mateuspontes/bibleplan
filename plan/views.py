from django.shortcuts import render

def home(request):
  return render(request, 'plan/index.html', {})