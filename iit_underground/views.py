from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponseForbidden
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.models import User
from .forms import PotinForm, CommentaireForm
from .models import Potin, Tag, Profil


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
    tag_actif = request.GET.get('tag')
    if tag_actif:
        potins = potins.filter(tags__nom=tag_actif)
    tags = Tag.objects.all()
    return render(request, 'iit_underground/fil.html', {
        'potins': potins,
        'tags': tags,
        'tag_actif': tag_actif,
    })


def detail_potin(request, potin_id):
    potin = get_object_or_404(Potin, id=potin_id)

    if request.method == 'POST':
        if not request.user.is_authenticated:
            return redirect('login')
        form = CommentaireForm(request.POST)
        if form.is_valid():
            commentaire = form.save(commit=False)
            commentaire.potin = potin
            commentaire.auteur = request.user
            commentaire.save()
            return redirect('iit_underground:detail', potin_id=potin.id)
    else:
        form = CommentaireForm()

    return render(request, 'iit_underground/detail.html', {
        'potin': potin,
        'form': form,
    })


@login_required
def creer_potin(request):
    if request.method == 'POST':
        form = PotinForm(request.POST, request.FILES)
        if form.is_valid():
            potin = form.save(commit=False)
            potin.auteur = request.user
            potin.save()
            form.save_m2m()
            return redirect('iit_underground:detail', potin_id=potin.id)
    else:
        initial = {}
        profil = getattr(request.user, 'profil', None)
        if profil:
            initial['anonyme'] = profil.anonyme_par_defaut
        form = PotinForm(initial=initial)
    return render(request, 'iit_underground/creer.html', {'form': form})


@login_required
def modifier_potin(request, potin_id):
    potin = get_object_or_404(Potin, id=potin_id)
    if potin.auteur != request.user:
        return HttpResponseForbidden("Tu ne peux modifier que tes propres posts.")
    if request.method == 'POST':
        form = PotinForm(request.POST, request.FILES, instance=potin)
        if form.is_valid():
            form.save()
            return redirect('iit_underground:detail', potin_id=potin.id)
    else:
        form = PotinForm(instance=potin)
    return render(request, 'iit_underground/modifier.html', {'form': form, 'potin': potin})


@login_required
def supprimer_potin(request, potin_id):
    potin = get_object_or_404(Potin, id=potin_id)
    if potin.auteur != request.user:
        return HttpResponseForbidden("Tu ne peux supprimer que tes propres posts.")
    if request.method == 'POST':
        potin.delete()
        return redirect('iit_underground:fil')
    return render(request, 'iit_underground/confirmer_suppression.html', {'potin': potin})


@login_required
def profil_utilisateur(request):
    profil, _ = Profil.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        if 'avatar' in request.FILES:
            profil.avatar = request.FILES['avatar']
        profil.anonyme_par_defaut = 'anonyme_par_defaut' in request.POST
        profil.save()
        return redirect('iit_underground:profil')

    mes_potins = request.user.potins.all()
    return render(request, 'iit_underground/profil.html', {
        'profil': profil,
        'mes_potins': mes_potins,
        'nb_potins': mes_potins.count(),
    })
