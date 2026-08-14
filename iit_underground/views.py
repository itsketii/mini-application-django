from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect
from django.shortcuts import render
from django.contrib.auth import login
from .forms import PotinForm
from .models import Potin


def inscription(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('iit_underground:fil')
    else:
        form = UserCreationForm()
    return render(request, 'iit_underground/inscription.html', {'form': form})


def fil_actualite(request):
    potins = Potin.objects.all()
    return render(request, 'iit_underground/fil.html', {'potins': potins})


def detail_potin(request, potin_id):
    potin = Potin.objects.get(id=potin_id)
    return render(request, 'iit_underground/detail.html', {'potin': potin})



@login_required
def creer_potin(request):
    if request.method == 'POST':
        form = PotinForm(request.POST, request.FILES)
        if form.is_valid():
            potin = form.save(commit=False)
            potin.auteur = request.user
            potin.save()
            form.save_m2m()
            return redirect('iit_underground:detail', pk=potin.pk)
    else:
        form = PotinForm()
    return render(request, 'iit_underground/creer.html', {'form': form})