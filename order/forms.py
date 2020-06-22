from django import forms
from .models import *
from django.contrib.admin.widgets import AdminDateWidget


class ApproveQuotationForm(forms.ModelForm):

    class Meta:
        model = OrderRegister
        fields = ['discount_rate',
                  'payment_advance']


class ConfirmOrderForm(forms.ModelForm):
    project = forms.ModelChoiceField(
        queryset=ProjectRegister.objects.all(), empty_label='Select Project')

    class Meta:
        model = OrderRegister
        fields = ['project']


class PaymentConfirmForm(forms.ModelForm):

    class Meta:
        model = OrderRegister
        fields = ['payment_received', ]


class DnCnForm(forms.ModelForm):
    truck_rate = forms.FloatField(widget=forms.NumberInput(attrs={'placeholder': 'Truck Rate', }),
                                  required=True)
    truck_type = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Type of Truck', }),
                                 required=True)
    truck_plate_num = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Truck plate Number', }),
                                      required=True)
    remarks = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Remarks', }),
                              required=False)

    class Meta:
        model = DnCnRegister
        exclude = ['order_register', 'recorded_by', 'type']
        # fields='__all__'


class RentConfirmForm(forms.ModelForm):
    class Meta:
        model = RentalDetails
        fields = ['expected_duration']


class RentIssueForm(forms.ModelForm):
    ordered_date = forms.DateField(widget=AdminDateWidget())

    class Meta:
        model = RentalDetails
        fields = ['ordered_date']


class RentReturnForm(forms.ModelForm):
    returned_date = forms.DateField(widget=AdminDateWidget())

    class Meta:
        model = RentalDetails
        fields = ['returned_date']
