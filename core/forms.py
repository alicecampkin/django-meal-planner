from django import forms
from .models import Member


class InitaliseHouseholdForm(forms.ModelForm):

    class Meta:
        model = Member
        fields = ['name', 'photo']


class MemberForm(forms.ModelForm):

    class Meta:
        model = Member
        fields = ['name', 'photo']
