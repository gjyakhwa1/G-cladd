import django_filters
from django.contrib.auth.models import User


class UserFilter(django_filters.FilterSet):
    CHOICES = (
        ('a', 'A-Z'),
        ('d', 'Z-A')
    )
    ordering = django_filters.ChoiceFilter(label='order', choices=CHOICES, method='sorting_method')

    def sorting_method(self, queryset, name, value):
        expression = 'username'if value == 'a' else '-username'
        return queryset.order_by(expression)

    class Meta:
        model = User
        fields = {
            'username': ['icontains'],
        }
