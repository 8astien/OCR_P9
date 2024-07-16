from django import forms


class FollowForm(forms.Form):
    username = forms.CharField(label="Nom d’utilisateur", max_length=150)
