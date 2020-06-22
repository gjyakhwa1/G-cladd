import django_filters
from .models import OrderRegister


class OrderFilter(django_filters.FilterSet):
    CHOICES=(
        ('a','Newest'),
         ('d','Oldest')
        )

    ordering=django_filters.ChoiceFilter(label='Order',choices=CHOICES, method='sorting_method')

    def sorting_method(self,queryset,name,value):
        expression= '-timestamp'if value=='a' else 'timestamp'
        return queryset.order_by(expression)

    class Meta:
        model=OrderRegister
        fields={'status',
                'type',
                'project',
           
            }