import django_filters
from account.models import Company


class CompanyFilter(django_filters.FilterSet):
    CHOICES=(
        ('a','A-Z'),
         ('d','Z-A')
        )
    ordering=django_filters.ChoiceFilter(label='order',choices=CHOICES, method='sorting_method')

    def sorting_method(self,queryset,name,value):
        expression= '-name'if value=='a' else 'name'
        return queryset.order_by(expression)

    class Meta:
        model=Company
        fields={
            'name':['icontains'],
            'city':['icontains']
            }