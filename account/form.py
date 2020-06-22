from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from account.models import Company, Profile


class CreateUserForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Username'}),
        required=True, max_length=50)
    first_name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'First Name', 'autofocus': 'True'}),
        required=True, max_length=50)
    last_name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
        required=True, max_length=50)
    email = forms.CharField(widget=forms.EmailInput(
        attrs={'class': 'form-control', 'placeholder': 'Email Address'}),
        required=True, max_length=50)
    password1 = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Password'}),
        required=True, max_length=50)
    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Confirm Password'}),
        required=True, max_length=50)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']

    def clean_email(self):
        email = self.cleaned_data['email']
        try:
            match = User.objects.get(email=email)
        except:
            return self.cleaned_data['email']
        raise forms.ValidationError("Email already exists")


class CreateProfileForm(forms.ModelForm):

    company = forms.ModelChoiceField(queryset=Company.objects.all(), empty_label="Select Company")
    account_type = forms.ChoiceField(
        choices=[('', 'Account Type')]+list(Profile.ACCOUNT_TYPE_CHOICES[1:]))
    contact_number = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Contact Number'}),
        required=True, max_length=50)

    def clean_account_type(self):
        account_type = self.cleaned_data['account_type']
        company = self.cleaned_data['company']

        if (account_type in ['SA', 'SU', 'YM'] and company.type != 'self'):
            raise forms.ValidationError(" Client Company cant have selected user types")
        if (account_type in ['CA', 'CU', 'PM'] and company.type == 'self'):
            raise forms.ValidationError(" Invalid Account type : Given Company is not client ")
        if (account_type == 'CA'):
            try:
                match = company.profile_set.get(account_type='CA')
            except:
                return self.cleaned_data['account_type']

            raise forms.ValidationError('Client Admin already exists for the given company ')
        return self.cleaned_data['account_type']

    class Meta:
        model = Profile
        fields = ['company', 'contact_number', 'account_type', 'profile_picture']
        # exclude=['user']


class UpdateUserForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Username'}),
        required=True, max_length=50)
    first_name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'First Name'}),
        required=True, max_length=50)
    last_name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
        required=True, max_length=50)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username']


class UpdateProfileForm(forms.ModelForm):

    def clean_username(self):
        username = self.cleaned_data['username']
        try:
            match = User.objects.get(username=username)
        except:
            return self.cleaned_data['username']
        raise forms.ValidationError('Username Already Exists ')

    class Meta:
        model = Profile
        fields = ['contact_number', 'profile_picture']
