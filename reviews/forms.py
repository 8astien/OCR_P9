from django import forms
from .models import Ticket, Review


class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ["title", "description", "image"]
        labels = {"title": "Titre", "description": "Description", "image": "Image"}

        widgets = {"title": forms.TextInput, "description": forms.Textarea, "image": forms.FileInput}


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ["rating", "headline", "body"]
        labels = {
            "rating": "Note",
            "headline": "Titre",
            "body": "Commentaire",
        }
        widgets = {
            "rating": forms.RadioSelect(choices=[(0, "0"), (1, "1"), (2, "2"), (3, "3"), (4, "4"), (5, "5")]),
            "headline": forms.TextInput(attrs={"class": "form-input"}),
            "body": forms.Textarea(attrs={"class": "form-input"}),
        }
