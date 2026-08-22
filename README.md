# IIT Underground

Mini-application Django de type réseau social / fil d’actualités, réalisée dans le cadre de la formation IIT Learn.

## Sujet

Le projet permet à un utilisateur de :

- s’inscrire et se connecter,
- publier des potins / articles courts,
- ajouter des tags,
- consulter un fil d’actualité,
- voir le détail d’un post,
- commenter un post,
- modifier ou supprimer ses propres publications,
- gérer son profil et son avatar,
- supprimer son compte.

---

## Fonctionnalités principales

- Authentification Django intégrée
- Création, lecture, mise à jour et suppression des posts
- Validation des formulaires
- Protection CSRF
- Accès réservé aux utilisateurs connectés pour les actions sensibles
- Modèle `Profil` avec avatar et option d’anonymat par défaut
- Modèle `Potin` avec relation `ForeignKey` et `ManyToManyField`
- Modèle `Commentaire` associé à un potin
- Interface HTML avec héritage de templates
- Admin Django personnalisé

---

## Structure du projet

```bash
mini-application-django/
├── config/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── iit_underground/
│   ├── migrations/
│   ├── static/
│   ├── templates/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── media/
├── db.sqlite3
├── manage.py
├── .gitignore
├── README.md
├── requirements.txt
└── venv/
```

---

## Prérequis

- Python 3.10+
- Django 5.x
- pip

---

## Installation

1. Cloner le projet

```bash
git clone https://github.com/itsketii/mini-application-django
cd mini-application-django
```

2. Créer un environnement virtuel

```bash
python -m venv venv
```

3. Activer l’environnement virtuel

Windows :

```bash
venv\Scripts\activate
```

Linux/macOS :

```bash
source venv/bin/activate
```

4. Installer les dépendances

```bash
pip install -r requirements.txt
```

5. Appliquer les migrations

```bash
python manage.py migrate
```

6. Lancer le serveur

```bash
python manage.py runserver
```

7. Ouvrir le projet dans le navigateur

```text
http://127.0.0.1:8000/
```

---

## Compte de test

Pour tester rapidement l’application, tu peux utiliser ce compte :

- Identifiant : admin_01
- Mot de passe : Password_1234

---

## Comptes et accès

- Les utilisateurs peuvent s’inscrire depuis la page d’inscription.
- La création, modification et suppression de posts nécessitent une connexion.
- La suppression du compte est possible depuis la page de profil.

---

## Fichiers importants

- [config/settings.py](config/settings.py) : configuration Django
- [config/urls.py](config/urls.py) : routes principales
- [iit_underground/models.py](iit_underground/models.py) : modèles ORM
- [iit_underground/views.py](iit_underground/views.py) : logique de l’application
- [iit_underground/forms.py](iit_underground/forms.py) : formulaires
- [iit_underground/admin.py](iit_underground/admin.py) : administration personnalisée
- [iit_underground/templates/iit_underground/base.html](iit_underground/templates/iit_underground/base.html) : template de base

---

## Documentation utilisée

- Django tutorial officiel
- Modèles et migrations Django
- Vues et templates Django
- Formulaires ModelForm
- Système d’authentification Django
- Protection CSRF

---

## Auteur

- Kouadio Ketsia Marie-Aude A.

Projet réalisé dans le cadre de la formation IIT Learn 25-26.
