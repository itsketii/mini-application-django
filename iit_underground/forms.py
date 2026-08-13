from django import forms
from .models import Potin


class PotinForm(forms.ModelForm):
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