from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponseForbidden
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from .forms import PostForm, CommentaireForm
from .models import Potin, Tag, Profil, Commentaire


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
    posts = Potin.objects.all()
    tag_actif = request.GET.get('tag')
    if tag_actif:
        posts = posts.filter(tags__nom=tag_actif)
    tags = Tag.objects.all()
    return render(request, 'iit_underground/fil.html', {
        'posts': posts,
        'tags': tags,
        'tag_actif': tag_actif,
    })


def detail_post(request, post_id):
    post = get_object_or_404(Potin, id=post_id)

    if request.method == 'POST':
        if not request.user.is_authenticated:
            return redirect('login')
        form = CommentaireForm(request.POST)
        if form.is_valid():
            commentaire = form.save(commit=False)
            commentaire.potin = post
            commentaire.auteur = request.user
            commentaire.save()
            return redirect('iit_underground:detail', post_id=post.id)
    else:
        form = CommentaireForm()

    return render(request, 'iit_underground/detail.html', {
        'post': post,
        'form': form,
    })


@login_required
def creer_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.auteur = request.user
            post.save()
            form.save_m2m()
            return redirect('iit_underground:detail', post_id=post.id)
    else:
        initial = {}
        profil = getattr(request.user, 'profil', None)
        if profil:
            initial['anonyme'] = profil.anonyme_par_defaut
        form = PostForm(initial=initial)
    return render(request, 'iit_underground/creer.html', {'form': form})


@login_required
def modifier_post(request, post_id):
    post = get_object_or_404(Potin, id=post_id)
    if post.auteur != request.user:
        return HttpResponseForbidden("Tu ne peux modifier que tes propres posts.")
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('iit_underground:detail', post_id=post.id)
    else:
        form = PostForm(instance=post)
    return render(request, 'iit_underground/modifier.html', {'form': form, 'post': post})


@login_required
def supprimer_post(request, post_id):
    post = get_object_or_404(Potin, id=post_id)
    if post.auteur != request.user:
        return HttpResponseForbidden("Tu ne peux supprimer que tes propres posts.")
    if request.method == 'POST':
        post.delete()
        return redirect('iit_underground:fil')
    return render(request, 'iit_underground/confirmer_suppression.html', {'post': post})


@login_required
def profil_utilisateur(request):
    profil, _ = Profil.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        if 'avatar' in request.FILES:
            profil.avatar = request.FILES['avatar']
        profil.anonyme_par_defaut = 'anonyme_par_defaut' in request.POST
        profil.save()
        return redirect('iit_underground:profil')

    mes_posts = request.user.potins.all()
    return render(request, 'iit_underground/profil.html', {
        'profil': profil,
        'mes_posts': mes_posts,
        'nb_posts': mes_posts.count(),
    })


@login_required
def supprimer_commentaire(request, commentaire_id):
    commentaire = get_object_or_404(Commentaire, id=commentaire_id)
    if commentaire.auteur != request.user:
        return HttpResponseForbidden("Tu ne peux supprimer que tes propres commentaires.")

    if request.method == 'POST':
        post_id = commentaire.potin.id
        commentaire.delete()
        return redirect('iit_underground:detail', post_id=post_id)

    return render(request, 'iit_underground/confirmer_suppression_commentaire.html', {
        'commentaire': commentaire,
    })


@login_required
def supprimer_compte(request):
    if request.method == 'POST':
        user = request.user
        logout(request)
        user.delete()
        return redirect('iit_underground:fil')

    return render(request, 'iit_underground/confirmer_suppression_compte.html', {
        'user': request.user,
    })
