from django import forms
from .models import StudentSemesterProfile,StudentProfile
from student.models import Result


class SearchResultForm(forms.Form):
    #semester = forms.ChoiceField(semester_choice, widget=forms.Select(attrs={'class': 'form-control'}))

    # semester_choice = (
    #
    #     ('4-2', '4th year 2nd semester'),
    #     ('4-1', '4th year 1st semester'),
    #     ('3-2', '3rd year 1st semester')
    # )


    semester_choice = (
        ('-----','--select--'),
        ( '4th year 2nd semester','4-2'),
        ( '4th year 1st semester','4-1',),
        ( '3th year 1st semester','3-2',)
    )
    semester = forms.ChoiceField(choices=semester_choice, widget=forms.Select(attrs={'class': 'form-control'}))
    roll = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    #semester = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))



class SearchStudentForm(forms.Form):
    roll = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    session = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))


widgets ={

            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'roll' : forms.TextInput(attrs={'class': 'form-control'}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'birthday': forms.TextInput(attrs={'class': 'form-control'}),
            'fathers_name' :forms.TextInput(attrs={'class': 'form-control'}),
            'address' : forms.Textarea(attrs={'class': 'form-control'}),
            'session' : forms.TextInput(attrs={'class': 'form-control'}),
            'mobile' :forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),

        }

class StudentProfileForm(forms.ModelForm):
    class Meta:
        model = StudentProfile
        fields ='__all__'

