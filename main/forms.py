from django import forms 

from main.models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model=Student
        fields='__all__'
        widgets={'name':forms.TextInput(attrs={'class':'myform'}),
        'password':forms.PasswordInput(attrs={'class':'passinput'})}