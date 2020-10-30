from django import forms
from .models import Meal
from core.models import Member

MEALTIME_CHOICES = [
    ('Breakfast', 'Breakfast'),
    ('Lunch', 'Lunch'),
    ('Dinner', 'Dinner'),
]


class CustomModelMultipleChoiceField(forms.ModelMultipleChoiceField):
    def label_from_instance(self, member):
        return "%s" % member.name


class CreateMealForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        """ Grants access to the request object so that only members of the current user
        are given as options"""

        self.request = kwargs.pop('request')
        super(CreateMealForm, self).__init__(*args, **kwargs)
        self.fields['members'].queryset = Member.objects.filter(
            user=self.request.user)

    class Meta:
        model = Meal
        fields = ['name', 'mealtime', 'date', 'members']

    name = forms.CharField()
    date = forms.DateInput()
    mealtime = forms.ChoiceField(choices=MEALTIME_CHOICES)
    members = CustomModelMultipleChoiceField(
        queryset=None,
        widget=forms.CheckboxSelectMultiple
    )
