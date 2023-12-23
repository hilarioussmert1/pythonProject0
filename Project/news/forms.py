from .models import News
from django import forms


class NewsForm(forms.ModelForm):
    description = forms.CharField(max_length=55)

    class Meta:
        model = News
        fields = [
            'name',
            'description',
            'category',
            'release_date',
        ]
