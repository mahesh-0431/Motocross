from django import forms
from .models import Candidate

from .models import OfferLetter

class CandidateForm(forms.ModelForm):
    class Meta:
        model = Candidate
        fields = ['name', 'address', 'designation', 'date_of_joining', 'salary']


class OfferLetterForm(forms.ModelForm):
    class Meta:
        model = OfferLetter
        fields = ['candidate', 'agreement_date', 'interviewer', 'referrer']