from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profil')
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    verifie = models.BooleanField(default=False)
    anonyme_par_defaut = models.BooleanField(default=True)

    def __str__(self):
        return f'Profil de {self.user.username}'


@receiver(post_save, sender=User)
def create_user_profil(sender, instance, created, **kwargs):
    if created:
        Profil.objects.create(user=instance)
    else:
        Profil.objects.get_or_create(user=instance)    

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