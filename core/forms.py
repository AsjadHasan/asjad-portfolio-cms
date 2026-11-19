"""Validated website contact form."""
from django import forms
from .models import ContactMessage


class ContactForm(forms.ModelForm):
    """Visitor message form with a simple honeypot field."""

    website = forms.CharField(required=False, widget=forms.TextInput(attrs={"tabindex": "-1", "autocomplete": "off"}))

    class Meta:
        model = ContactMessage
        fields = ["name", "email", "message"]
        widgets = {
            "name": forms.TextInput(attrs={"placeholder": "Your name", "autocomplete": "name"}),
            "email": forms.EmailInput(attrs={"placeholder": "you@example.com", "autocomplete": "email"}),
            "message": forms.Textarea(attrs={"placeholder": "Tell me about your project or opportunity...", "rows": 5}),
        }

    def clean_website(self):
        """Reject obviously automated submissions."""
        value = self.cleaned_data["website"]
        if value:
            raise forms.ValidationError("Unable to process this submission.")
        return value
