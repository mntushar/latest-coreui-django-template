from django import forms
from django.forms import ModelForm
from .models import*


#user loging form
class UserLogingForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':"Your Name", 'required':'True'}))
    password = forms.CharField(max_length=50, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder':"Enter Password", 'required':'True'}))


#user information form
class UserInfoForm(ModelForm):
    class Meta:
        model = UserInfo
        exclude = ['password']
        widgets = {
            'name' : forms.TextInput(attrs={'class':'form-control', 'required':'True'}),
            'gender' : forms.Select(attrs={'class':'form-control', 'required':'True'}),
            'date_of_birth' : forms.DateInput(attrs={'class':'form-control', 'type':'date', 'required':'True'}),
            'phone_number' : forms.NumberInput(attrs={'class':'form-control', 'required':'True'}),
            'email' : forms.EmailInput(attrs={'class':'form-control', 'required':'True'}),
            'occupation' : forms.TextInput(attrs={'class':'form-control', 'required':'True'}),
            'home_address' : forms.Textarea(attrs={'class':'form-control', 'required':'True'}),
            
        }


#user password forms
class UserPassForm(forms.Form):
    password = forms.CharField(max_length=50, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder':"Enter Password", 'required':'True'}))
    repassword = forms.CharField(max_length=50, label='Repeat Password', widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder':"Enter Password", 'required':'True'}))


#user password change forms
class UserPassChangeForm(forms.Form):
    password = forms.CharField(max_length=50, label='Enter New Password', widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder':"Enter Password", 'required':'True'}))
    repassword = forms.CharField(max_length=50, label='Repeat Password', widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder':"Enter Password", 'required':'True'}))


#password reset mail
class PassResetForm(forms.Form):
    mail = forms.EmailField(max_length=50, label='Enter user mail id', widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder':"Enter Password", 'required':'True'}))