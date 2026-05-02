from django import forms
from Clients.models import Client


class ClientForm(forms.ModelForm):
    motDePasse = forms.CharField(
        label='Mot de passe',
        required=False,
        widget=forms.PasswordInput(render_value=False),
        help_text='Laisser vide pour conserver le mot de passe actuel.',
    )

    class Meta:
        model = Client
        fields = ['nom', 'prenom', 'email', 'telephone', 'adresse', 'motDePasse']
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'w-full rounded-lg border border-border-light px-4 py-2'}),
            'prenom': forms.TextInput(attrs={'class': 'w-full rounded-lg border border-border-light px-4 py-2'}),
            'email': forms.EmailInput(attrs={'class': 'w-full rounded-lg border border-border-light px-4 py-2'}),
            'telephone': forms.TextInput(attrs={'class': 'w-full rounded-lg border border-border-light px-4 py-2'}),
            'adresse': forms.TextInput(attrs={'class': 'w-full rounded-lg border border-border-light px-4 py-2'}),
        }

    def save(self, commit=True):
        client = super().save(commit=False)
        if self.cleaned_data.get('motDePasse'):
            client.motDePasse = self.cleaned_data['motDePasse']
        else:
            client.motDePasse = self.instance.motDePasse
        if commit:
            client.save()
        return client
