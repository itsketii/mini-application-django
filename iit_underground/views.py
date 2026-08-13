from django.shortcuts import render
from .models import Potin


def fil_actualite(request):
    potins = Potin.objects.all()
    return render(request, 'iit_underground/fil.html', {'potins': potins})


def detail_potin(request, potin_id):
    potin = Potin.objects.get(id=potin_id)
    return render(request, 'iit_underground/detail.html', {'potin': potin})