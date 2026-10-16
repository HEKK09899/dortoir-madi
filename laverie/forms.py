from django import forms
from django.utils import timezone
from .models import Machine, FonctionMachine, Reservation, MessageLaverie


class MessageLaverieForm(forms.ModelForm):
    class Meta:
        model = MessageLaverie
        fields = ('texte', 'texte_ru', 'texte_en', 'ordre', 'active')

        labels = {
            'texte': 'Annonce en français',
            'texte_ru': 'Annonce en russe',
            'texte_en': 'Annonce en anglais',
            'ordre': "Ordre d'affichage",
            'active': 'Annonce active',
        }

        widgets = {
            'texte': forms.TextInput(attrs={
                'class': 'w-full px-4 py-2.5 border border-gray-300 rounded-xl focus:ring-2 focus:ring-teal-500 focus:border-teal-500',
                'placeholder': 'Ex. : Veuillez récupérer votre linge à l’heure.',
            }),
            'texte_ru': forms.TextInput(attrs={
                'class': 'w-full px-4 py-2.5 border border-gray-300 rounded-xl focus:ring-2 focus:ring-teal-500 focus:border-teal-500',
                'placeholder': 'Например: Пожалуйста, забирайте бельё вовремя.',
            }),
            'texte_en': forms.TextInput(attrs={
                'class': 'w-full px-4 py-2.5 border border-gray-300 rounded-xl focus:ring-2 focus:ring-teal-500 focus:border-teal-500',
                'placeholder': 'Example: Please collect your laundry on time.',
            }),
            'ordre': forms.NumberInput(attrs={
                'class': 'w-full px-4 py-2.5 border border-gray-300 rounded-xl focus:ring-2 focus:ring-teal-500 focus:border-teal-500',
                'min': 0,
            }),
            'active': forms.CheckboxInput(attrs={
                'class': 'rounded border-gray-300 text-teal-600 focus:ring-teal-500',
            }),
        }        
class MachineForm(forms.ModelForm):
    class Meta:
        model = Machine
        fields = ('nom', 'ordre', 'active')
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'w-full px-4 py-2.5 border border-gray-300 rounded-xl focus:ring-2 focus:ring-teal-500 focus:border-teal-500', 'placeholder': 'Ex: Machine 1'}),
            'ordre': forms.NumberInput(attrs={'class': 'w-full px-4 py-2.5 border border-gray-300 rounded-xl focus:ring-2 focus:ring-teal-500 focus:border-teal-500', 'min': 0}),
            'active': forms.CheckboxInput(attrs={'class': 'rounded border-gray-300 text-teal-600 focus:ring-teal-500'}),
        }


class FonctionMachineForm(forms.ModelForm):
    class Meta:
        model = FonctionMachine
        fields = (
            'machine',
            'nom',
            'nom_ru',
            'nom_en',
            'duree_minutes',
            'ordre',
            'active',
        )

        labels = {
            'machine': 'Machine',
            'nom': 'Nom du programme en français',
            'nom_ru': 'Nom du programme en russe',
            'nom_en': 'Nom du programme en anglais',
            'duree_minutes': 'Durée en minutes',
            'ordre': "Ordre d'affichage",
            'active': 'Programme actif',
        }

        widgets = {
            'machine': forms.Select(attrs={
                'class': 'w-full px-4 py-2.5 border border-gray-300 rounded-xl focus:ring-2 focus:ring-teal-500 focus:border-teal-500',
            }),
            'nom': forms.TextInput(attrs={
                'class': 'w-full px-4 py-2.5 border border-gray-300 rounded-xl focus:ring-2 focus:ring-teal-500 focus:border-teal-500',
                'placeholder': 'Ex : Coton, Jeans',
            }),
            'nom_ru': forms.TextInput(attrs={
                'class': 'w-full px-4 py-2.5 border border-gray-300 rounded-xl focus:ring-2 focus:ring-teal-500 focus:border-teal-500',
                'placeholder': 'Ex : Хлопок, Джинсы',
            }),
            'nom_en': forms.TextInput(attrs={
                'class': 'w-full px-4 py-2.5 border border-gray-300 rounded-xl focus:ring-2 focus:ring-teal-500 focus:border-teal-500',
                'placeholder': 'Ex : Cotton, Jeans',
            }),
            'duree_minutes': forms.NumberInput(attrs={
                'class': 'w-full px-4 py-2.5 border border-gray-300 rounded-xl focus:ring-2 focus:ring-teal-500 focus:border-teal-500',
                'min': 1,
            }),
            'ordre': forms.NumberInput(attrs={
                'class': 'w-full px-4 py-2.5 border border-gray-300 rounded-xl focus:ring-2 focus:ring-teal-500 focus:border-teal-500',
                'min': 0,
            }),
            'active': forms.CheckboxInput(attrs={
                'class': 'rounded border-gray-300 text-teal-600 focus:ring-teal-500',
            }),
        }
class ReservationForm(forms.ModelForm):
    """Réservation : choix machine et programme. Le créneau est placé automatiquement après le dernier ticket actif."""
    class Meta:
        model = Reservation
        fields = ('machine', 'fonction')

    
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        initial = kwargs.get('initial') or {}
        super().__init__(*args, **kwargs)

        initial_machine = initial.get('machine')
        machines_qs = Machine.objects.filter(active=True)

        if user and user.user_type == "ETUDIANT":
            if user.dortoir:
                machines_qs = machines_qs.filter(
                    dortoir=user.dortoir
                )
            else:
                machines_qs = machines_qs.none()

        self.fields['machine'].queryset = machines_qs
        if (
    initial_machine
    and machines_qs.filter(
        pk=getattr(initial_machine, 'pk', initial_machine)
    ).exists()
):
            self.fields['fonction'].queryset = FonctionMachine.objects.filter(machine=initial_machine, active=True)
        else:
            self.fields['fonction'].queryset = FonctionMachine.objects.filter(
    active=True,
    machine__in=machines_qs
)
        self.fields['fonction'].required = True
        self.fields['fonction'].label_from_instance = lambda obj: f"{obj.nom} — {obj.duree_affichage()}"
        self.fields['fonction'].widget.attrs['class'] = 'select-resa w-full pl-4 pr-10 py-3 border border-gray-300 rounded-xl focus:ring-2 focus:ring-teal-500 focus:border-teal-500 bg-white cursor-pointer text-gray-900 shadow-sm appearance-none'
        self.fields['machine'].widget.attrs['class'] = 'select-resa w-full pl-4 pr-10 py-3 border border-gray-300 rounded-xl focus:ring-2 focus:ring-teal-500 focus:border-teal-500 bg-white cursor-pointer text-gray-900 shadow-sm appearance-none'

    def _get_debut_apres_dernier_ticket(self, machine):
        """Retourne le début du prochain créneau = fin du dernier ticket + 5 min (retrait/remise du linge)."""
        from datetime import timedelta
        now = timezone.now()
        dernier = (
            Reservation.objects.filter(
                machine=machine,
                statut__in=('reserve', 'en_cours'),
                fin__gt=now,
            )
            .order_by('-fin')
            .first()
        )
        if dernier:
            return dernier.fin + timedelta(minutes=5)
        # Personne sur la machine : on laisse 5 minutes à l'utilisateur pour se préparer
        return now + timedelta(minutes=5)

    def clean(self):
        data = super().clean()
        machine = data.get('machine')
        fonction = data.get('fonction')

        if not machine or not fonction:
            return data
        if fonction.machine_id != machine.id:
            self.add_error('fonction', 'Cette fonction n\'appartient pas à la machine choisie.')
        return data

    def save(self, commit=True):
        from datetime import timedelta
        instance = super().save(commit=False)
        instance.debut = self._get_debut_apres_dernier_ticket(instance.machine)
        instance.fin = instance.debut + timedelta(minutes=instance.fonction.duree_minutes)
        if commit:
            instance.save()
        return instance
