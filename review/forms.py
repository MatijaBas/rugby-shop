from django import forms
from .models import Review


class ReviewSharingForm(forms.ModelForm):

    class Meta:
        model = Review
        fields = ('title', 'content', 'published_date')
