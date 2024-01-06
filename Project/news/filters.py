import django_filters
from django_filters import FilterSet, ModelChoiceFilter, DateFilter, CharFilter
from django import forms
from .models import News, Category


class NewsFilter(FilterSet):
    category = ModelChoiceFilter(
        queryset=Category.objects.all(),
        empty_label='любой',
        label='Категория'
    )
    release_date = DateFilter(
        field_name='release_date',
        widget=forms.DateInput(attrs={'type': 'date'}),
        lookup_expr='date__gte',
        label='Дата выпуска число которое позже данного',
    )

    class Meta:
        model = News
        fields = {
            'name': ['icontains'],
            'category': ['exact'],
            'release_date': ['exact'],
        }