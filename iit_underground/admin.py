from django.contrib import admin
from .models import Tag, Potin, Commentaire


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    search_fields = ('nom',)


@admin.register(Potin)
class PotinAdmin(admin.ModelAdmin):
    list_display = ('titre', 'auteur', 'anonyme', 'date_publication')
    list_filter = ('anonyme', 'tags')
    search_fields = ('titre', 'contenu')


@admin.register(Commentaire)
class CommentaireAdmin(admin.ModelAdmin):
    list_display = ('potin', 'auteur', 'date_publication')