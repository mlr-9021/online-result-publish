from django import forms
from .models import TeacherProfile



class SearchTeacherForm(forms.Form):
    name = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    mobile = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))



class TeacherForm(forms.ModelForm):
    class Meta:
        model = TeacherProfile
        fields ='__all__'


widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'designation': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
        }

