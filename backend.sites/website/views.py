from django.shortcuts import render, redirect
from .form import *

def home (request):
    return render(request , 'index.html')

def home(request):
    # uy = Home.objects.all()
    # context = {
    #     "home": uy
    # }
    return render(request, 'index.html', )

def base(request):
    if request.method == 'POST':
        form = Sign(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = Sign()
        
    context = {
        "form": form,
    }
    return render(request, 'base.html', context)

def chart(request):
    # uy = Home.objects.all()
    # context = {
    #     "chart": uy,
    # }
    return render(request, 'chart.html', )
