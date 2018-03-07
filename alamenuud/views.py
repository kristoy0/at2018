from django.shortcuts import render
from .models import Alamenuu, Sundmus

# Create your views here.
def index(request):
    menuud = Alamenuu.objects.all()

    context = {
        'menuud': menuud
    }

    return render(request, 'alamenuud/index.html', context)

def muud(request, leht):
    menuud = Alamenuu.objects.all()
    sisu = Alamenuu.objects.get(nimetus=leht)

    context = {
        'menuud': menuud,
        'sisu': sisu
    }

    return render(request, 'alamenuud/muud.html', context)

def sundmused(request):
    menuud = Alamenuu.objects.all()
    kalender = Sundmus.objects.all()

    context = {
        'menuud': menuud,
        'kalender': kalender
    }

    return render(request, 'alamenuud/sundmused.html', context)