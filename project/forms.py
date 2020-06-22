from django import forms
from .models import ProjectRegister
from account.models import Company
from django.contrib.auth.models import User
from django.db.models import Q

class addProjectForm(forms.ModelForm):
    #COMPANY_CHOICE=[('','Select Company')]+list([(company.pk,company.name) for company in Company.objects.all()])
    #PLACEHOLDER=(('','Select Company'),('','sd'))
    #COMPANY_CHOICE= PLACEHOLDER+COMPANY_LIST
    #COMPANY_CHOICE=tuple([(Company.objects.get(id=company.id),company.name) for company in Company.objects.all()])
    #company=forms.ChoiceField(widget=forms.Select(), choices=COMPANY_CHOICE)
    company=forms.ModelChoiceField(queryset=Company.objects.filter(type='client'),empty_label="Select Company")
    projectTitle=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Project Title'}),
                                 required=True,max_length=100)
    projectId=forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder':'Project ID'}),
                                 required=True)
    projectContractNo=forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder':'Project Contract No'}),
                                 required=True)
    projectSiteLocation=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Project Site Location'}),
                                 required=True,max_length=100)
    projectMailLocation=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Project Mail Location'}),
                                 required=False,max_length=100)
    orderNumber=forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder':'Order Number'}),
                                 required=True)
    projectStatus=forms.ChoiceField(choices=[('','Project Status')]+list(ProjectRegister.STATUS_TYPES))
    
    txTruckRates=forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder':'Tx Truck Rates'}),
                                 required=True)
    remarks=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Remarks'}),
                                 required=False,max_length=200)
    projectRecordedBy=forms.ModelChoiceField(queryset=User.objects.all(),required=False,widget=forms.HiddenInput())
   
        
    def _clean_fields(self):
        
        #field['company']=Company.objects.get(pk=field['company'])
        #company=Company.objects.get(pk=self.fields['company'])
        print(self.fields['projectRecordedBy'])
        return super()._clean_fields()
        
    class Meta:
        model=ProjectRegister
        #fields='__all__'
        fields=['company',
                'projectTitle',
                'projectId',
                'projectContractNo',
                'projectSiteLocation',
                'projectMailLocation',
                'orderNumber',
                'projectStatus',
                'txTruckRates',
                'remarks',
                'projectRecordedBy'
                ]
