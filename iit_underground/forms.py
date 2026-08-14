from django import forms
from .models import Commentaire, Potin


class PostForm(forms.ModelForm):
    class Meta:
        model = Potin
        fields = ['titre', 'contenu', 'image', 'tags', 'anonyme']
        widgets = {
            'contenu': forms.Textarea(attrs={'rows': 6}),
        }

        def clean_titre(self):
            titre = self.cleaned_data.get('titre')
            if len(titre) < 5:
                raise forms.ValidationError("Le titre doit contenir au moins 5 caractères.")
            return titre


class CommentaireForm(forms.ModelForm):
    class Meta:
        model = Commentaire
        fields = ['contenu']
        widgets = {
            'contenu': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Ajouter un commentaire...'}),
        }
        labels = {
            'contenu': '',
        }  