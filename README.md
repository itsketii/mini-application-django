# FORMATION L2 - MINI-APPLICATION DJANGO : IIT UNDERGROUND

### Description

Dans le cadre de la formation IIT Learn 25-26, ce dépôt contient le projet Django nommé `config` et l'application `iit_underground`. L'objectif est de mettre en pratique les bases du framework Django, en développant une mini-application de type réseau social où l'on peut publier des potins, consulter un fil d'actualité et gérer les publications.

Ce projet permet de travailler sur :

- la création d'un projet et d'une application Django,
- l'architecture MVT,
- la définition de modèles et l'utilisation de l'ORM,
- la création de vues et de templates,
- la gestion des utilisateurs et des publications,
- la collaboration avec Git et GitHub.

---

### Objectifs validés

* Créer un projet Django et une application, et comprendre l'architecture MVT
* Définir un modèle, générer et appliquer une migration, manipuler les données via l'ORM
* Créer des vues qui utilisent l'ORM et des templates pour afficher les résultats
* Gérer les fonctionnalités principales d'une application web Django
* Travailler en équipe via Git et résoudre les conflits éventuels

---

### Travail réalisé

* [X] Créer le dépôt GitHub et le cloner localement
* [X] Créer un environnement virtuel
* [X] Installer Django
* [X] Créer le projet Django `config`
* [X] Créer l'application Django `iit_underground`
* [X] Déclarer l'application dans `INSTALLED_APPS`
* [X] Vérifier le démarrage du serveur Django
* [X] Configurer le fichier `.gitignore`
* [ ] Créer le modèle `Post` et ses relations
* [ ] Gérer les utilisateurs et les commentaires
* [ ] Créer les vues principales : inscription, fil d'actualité, détail, création, modification, suppression
* [ ] Développer les templates HTML de l'application
* [ ] Configurer les URLs de l'application
* [ ] Mettre en place la gestion des images et des médias

---

### Configuration de l'environnement

##### 1. Clonage du projet

```bash
git clone https://github.com/itsketii/mini-application-django.git
cd mini-application-django
```

##### 2. Environnement virtuel Python

```bash
python -m venv venv
```

Activation :

```bash
# Windows
venv\Scripts\activate

# Linux/macOS
source venv/bin/activate
```

#### 3. Dépendances installées

* `django`
* `pillow` (pour la gestion des images)

##### 4. Lancement du projet

```bash
python manage.py migrate
python manage.py runserver
```

Puis ouvrir :

```bash
http://127.0.0.1:8000/
```

---

### Structure du projet

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
│   ├── templates/
│   ├── static/
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
├── venv/
└── requirements.txt
```

---

### Description du projet

Le projet est une application web de type réseau social minimal, nommée `iit_underground`. Elle permet à un utilisateur de :

- s'inscrire,
- se connecter,
- créer des publications,
- consulter un fil d'actualité,
- voir le détail d'une publication,
- modifier ou supprimer ses propres posts,
- ajouter une image à un potin.

---

### Collaboration & Workflow Git

- Collaborateurs invités : @sedrickgael & @junmodeste

---

### Documentation utilisée

* [Django : Tutoriel officiel, partie 1](https://docs.djangoproject.com/fr/5.1/intro/tutorial01/)
* [Django : Tutoriel officiel, partie 2](https://docs.djangoproject.com/fr/5.1/intro/tutorial02/)
* [Django : Référence des requêtes ORM (QuerySet)](https://docs.djangoproject.com/fr/5.1/topics/db/queries/)
* [Django : Tutoriel officiel, partie 3](https://docs.djangoproject.com/fr/5.1/intro/tutorial03/)
* [Django : Tutoriel officiel, partie 4](https://docs.djangoproject.com/fr/5.1/intro/tutorial04/)
* [Django : Héritage de templates](https://docs.djangoproject.com/fr/5.1/ref/templates/language/#template-inheritance)

---

### Conclusion

Ce projet a permis de comprendre les bases de Django et de mettre en pratique les notions essentielles du développement web avec Python : création d'un projet, modélisation des données, interactions avec la base de données et affichage des informations via des vues et des templates. Il a aussi permis de renforcer les compétences en collaboration avec Git et GitHub dans le cadre d'un travail collaboratif.

---

### Auteurs

* Kouadio Ketsia Marie-Aude A. (@itsketii)

Projet réalisé dans le cadre de la formation IIT Learn 25-26.
