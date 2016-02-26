from django import forms


class ConnectForm(forms.Form):
    username = forms.CharField(label="Utilisateur",max_length=30)
    password = forms.CharField(label="Mot de passe",widget=forms.PasswordInput)