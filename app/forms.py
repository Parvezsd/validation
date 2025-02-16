from django import forms
from app.models import *
def validate_for_char(data):
    if not data[0].isalpha():
        raise forms.ValidationError('error')
    

def validate_for_len(value):
    if len(value)<5:
        raise forms.ValidationError('error')

class StudentForms(forms.Form):
    StudentId=forms.IntegerField()
    Student_name=forms.CharField(validators=[validate_for_char,validate_for_len])
    Student_email=forms.EmailField(validators=[validate_for_char])
    Student_remail=forms.EmailField()
    
    def clean(self):
        e=self.cleaned_data['Student_email']
        re=self.cleaned_data['Student_remail']
        if e!=re:
            raise forms.ValidationError('error')
        return super().clean()