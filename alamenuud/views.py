from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Alamenuu, Sundmus, Uudis

# Create your views here.
def index(request):
    menuud = Alamenuu.objects.all()
    uudiste_nimekiri = Uudis.objects.order_by('-kuupaev')

    paginator = Paginator(uudiste_nimekiri, 2)

    page = request.GET.get('page')
    uudised = paginator.get_page(page)

    context = {
        'menuud': menuud,
        'uudised': uudised
    }

    return render(request, 'alamenuud/index.html', context)

def muud(request, leht):
    menuud = Alamenuu.objects.all()
    if leht != "favicon.ico":
        try:
            sisu = Alamenuu.objects.get(nimetus=leht)
        except Alamenuu.DoesNotExist:
            sisu = None
    else:
        sisu = None


    context = {
        'menuud': menuud,
        'sisu': sisu
    }

    return render(request, 'alamenuud/muud.html', context)

def postitus(request, number):
    menuud = Alamenuu.objects.all()
    sisu = Uudis.objects.get(id=number)

    context = {
        'menuud': menuud,
        'sisu': sisu,
        'post': True
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
