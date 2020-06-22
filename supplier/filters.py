import django_filters
from .models import SupplierRegister


class SupplierFilter(django_filters.FilterSet):
    CHOICES=(
        ('a','A-Z'),
         ('d','Z-A')
        )
    ordering=django_filters.ChoiceFilter(label='order',choices=CHOICES, method='sorting_method')

    def sorting_method(self,queryset,name,value):
        expression= 'supplierName'if value=='a' else '-supplierName'
        return queryset.order_by(expression)

    class Meta:
        model=SupplierRegister
        fields={
            'supplierName':['icontains'],
            'supplierAddress':['icontains']
            }