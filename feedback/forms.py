from django import forms
from .models import Feedback

class ReponseForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['nom', 'email', 'avis']