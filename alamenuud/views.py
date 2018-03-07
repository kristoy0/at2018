from django.shortcuts import render
from .models import Alamenuu

# Create your views here.
def index(request):

    menuud = Alamenuu.objects.all()

    context = {
        'menuud': menuud
    }

    return render(request, 'alamenuud/index.html', context)
