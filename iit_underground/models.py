from django.db import models
from django.contrib.auth.models import User

class Tag(models.Model):
    nom = models.CharField(max_length=50)

    def __str__(self):
        return self.nom


class Potin(models.Model):
    titre = models.CharField(max_length=200)
    contenu = models.TextField()
    image = models.ImageField(upload_to='potins/', blank=True, null=True)
    auteur = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='potins'
    )
    anonyme = models.BooleanField(default=True)
    date_publication = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(Tag, related_name='potins', blank=True)

    def __str__(self):
        return self.titre

    class Meta:
        ordering = ['-date_publication']


class Commentaire(models.Model):
    potin = models.ForeignKey(Potin, on_delete=models.CASCADE, related_name='commentaires')
    auteur = models.ForeignKey(User, on_delete=models.CASCADE)
    contenu = models.TextField()
    date_publication = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Commentaire de {self.auteur.username} sur {self.potin}'

    class Meta:
        ordering = ['-date_publication']