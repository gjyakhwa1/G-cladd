import django_filters
from .models import ProjectRegister
from account.models import Company


class ProjectFilter(django_filters.FilterSet):
    CHOICES=(
        ('a','A-Z'),
         ('d','Z-A')
        )
    
    ordering=django_filters.ChoiceFilter(label='order',choices=CHOICES, method='sorting_method')

    def sorting_method(self,queryset,name,value):
        expression= 'projectTitle'if value=='a' else '-projectTitle'
        return queryset.order_by(expression)

    class Meta:
        model=ProjectRegister
        fields={
            'projectTitle':['icontains'],
            'projectSiteLocation':['icontains'],

            }