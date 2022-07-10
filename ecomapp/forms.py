from django import forms
from .models import Review

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email_address = forms.EmailField(max_length = 150)
    subject = forms.CharField(max_length=150)
    message = forms.CharField(widget = forms.Textarea, max_length = 3000)

class ReviewForm(forms.ModelForm):
    review = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={'class':'text-input', 'placeholder':''}),
    )
    
    class Meta:
        model = Review
        fields = ('review',)