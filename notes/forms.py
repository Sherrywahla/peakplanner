from django import forms
from .models import Note

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ["title", "content", "priority", "status"]
        widgets = {
            "priority": forms.Select(attrs={
                "class": "bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:text-white",
            }, choices=[
                ("Low", "Low"),
                ("Medium", "Medium"),
                ("High", "High"),
            ]),
        }
