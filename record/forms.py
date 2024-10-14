from django import forms
from django.core.exceptions import ValidationError

from .models import StudentAssessmentRecord

class StudentAssessmentRecordForm(forms.ModelForm):
    class Meta:
        model = StudentAssessmentRecord
        fields = ['score']
        labels = {
            'score': 'Student Record'
        }
        widgets = {
            'score': forms.TextInput(attrs={'class': 'form-control my-2'}),
        }