from account.models import Company
from django import forms

from django.core.exceptions import ValidationError

class AddCompanyForm(forms.ModelForm):
    
    def clean_type(self):
        if self.cleaned_data['type']=='self':
            
            try:
                match=Company.objects.get(type='self')
                print(match.type)
            except:
                return self.cleaned_data['type']
            raise ValidationError('Company with account type "self" already exists')
        return self.cleaned_data['type']


    class Meta:
        model=Company
        fields=['name',
                'country',
                'province',
                'city',
                'street',
                'type',
                'contact_number',
                'website',
                'remarks']