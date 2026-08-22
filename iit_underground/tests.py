from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from iit_underground.models import Potin


class PotinModelTest(TestCase):
    def test_creation_potin(self):
        user = User.objects.create_user(username='Testeur_1', password='mdp123')
        potin = Potin.objects.create(
            titre='Premier post',
            contenu='Contenu test',
            auteur=user,
            anonyme=True,
        )
        self.assertEqual(potin.titre, 'Premier post')


class SuppressionCompteTest(TestCase):
    def test_supprimer_compte_connecte(self):
        user = User.objects.create_user(username='Testeur_1', password='mdp123')
        self.client.login(username='Testeur_1', password='mdp123')

        response = self.client.post(reverse('iit_underground:supprimer_compte'))

        self.assertEqual(response.status_code, 302)
        self.assertFalse(User.objects.filter(username='Testeur_1').exists())
