from django_filters import FilterSet, ModelChoiceFilter, ModelMultipleChoiceFilter
from .models import Product, Material


class ProductFilter(FilterSet):
    material = ModelChoiceFilter(
        field_name='productmaterial__material',
        queryset=Material.objects.all(),
        label='Material',
        empty_label='любой'
    )

    class Meta:
        model = Product
        fields = {
            'name': ['icontains'],
            'quantity': ['gt'],
            'price': ['lt', 'gt', ],
        }
