from django import forms
from .models import User
class EmployeeRegistration(forms.ModelForm):
    class Meta:
        model=User
        fields="__all__" 
        widgets = {
   'name': forms.TextInput(attrs={'class':'form-control'}),
   'email': forms.EmailInput(attrs={'class':'form-control'}),
   'password': forms.PasswordInput( attrs={'class':'form-control'}),
  }
    def clean_name(self):
        valname = self.cleaned_data['name']
        if len(valname) < 4:
            raise forms.ValidationError('Enter more than or equal 4 char')
        return valname

    def clean_email(self):
        ealname = self.cleaned_data['email']
        if not "@gmail.com" in ealname :
            raise forms.ValidationError('Enter email with gmail id only')
        return ealname