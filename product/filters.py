import django_filters
from .models import ProductRegister


class ProductFilter(django_filters.FilterSet):
    CHOICES = (
        ('a', 'A-Z'),
        ('d', 'Z-A')
    )
    ordering = django_filters.ChoiceFilter(label='order', choices=CHOICES, method='sorting_method')

    def sorting_method(self, queryset, name, value):
        expression = 'productName'if value == 'a' else '-productName'
        return queryset.order_by(expression)

    class Meta:
        model = ProductRegister
        fields = {
            'productName': ['icontains'],
            'productItemCode': ['icontains']
        }
