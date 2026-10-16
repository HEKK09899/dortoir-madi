
from django import forms
from .models import DemandeDevis


class DemandeDevisForm(forms.ModelForm):
    class Meta:
        model = DemandeDevis

        fields = [
            "nom",
            "entreprise",
            "email",
            "telephone",
            "service",
            "budget",
            "message",
        ]

        labels = {
            "nom": "Votre nom complet",
            "entreprise": "Nom de votre entreprise",
            "email": "Adresse e-mail",
            "telephone": "Téléphone",
            "service": "Quel service vous intéresse ?",
            "budget": "Budget estimé",
            "message": "Décrivez votre projet",
        }

        widgets = {
            "nom": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Ex. : Jean Dupont",
            }),
            "entreprise": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Nom de votre entreprise (facultatif)",
            }),
            "email": forms.EmailInput(attrs={
                "class": "form-control",
                "placeholder": "vous@exemple.com",
            }),
            "telephone": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Votre numéro (facultatif)",
            }),
            "service": forms.Select(attrs={
                "class": "form-control",
            }),
            "budget": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Ex. : 3 000 à 5 000 DH",
            }),
            "message": forms.Textarea(attrs={
                "class": "form-control",
                "rows": 5,
                "placeholder": "Présentez votre besoin et vos objectifs...",
            }),
        }
