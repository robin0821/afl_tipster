from django.db.models import fields
from crispy_forms.helper import FormHelper
from django import forms
from crispy_forms.layout import Submit, Layout, Div
from crispy_forms.bootstrap import PrependedText, InlineRadios
from .models import AFLFixture, AFLTeams, tippings
from django.forms import formset_factory, modelformset_factory, HiddenInput
from django.utils.safestring import mark_safe

class DataFreshForm(forms.Form):
    update_choices = (
        ('Refresh Fixture', 'Refresh Fixture'),
        ('Refresh Tippings', 'Refresh Tippings'),
        ('Refresh Tipping Ladder', 'Refresh Tipping Ladder'),
        ('AFL Ladder', 'AFL Ladder')
    )

    refresh_options = forms.ChoiceField(choices=update_choices, initial='Refresh Fixture')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        helper = self.helper = FormHelper()
        self.helper.form_id = 'data-refresh-form'
        self.helper.add_input(Submit('submit', 'Submit'))
        self.helper.form_class = 'blueForms'
        self.helper.form_method = 'get'
        self.helper.form_action = ''
        helper.form_show_labels = True

class TippingForm(forms.ModelForm):
    class Meta:
        model = tippings
        fields = ['first_name', 'last_name', 'email', 'fixture_id', 'picks', 'margin', 'hteam', 
                  'ateam', 'hteam_url', 'ateam_url', 'date', 'venue', 'status', 'winner', 'disabled']
        widget = {'first_name': forms.HiddenInput(),
                  'last_name': forms.HiddenInput(), 
                  'email': forms.HiddenInput(), 
                  'fixture_id': forms.HiddenInput(),
                  'hteam': forms.HiddenInput(),
                  'ateam': forms.HiddenInput(),
                  'hteam_url': forms.HiddenInput(),
                  'ateam_url': forms.HiddenInput(),
                  'date': forms.HiddenInput(),
                  'venue': forms.HiddenInput(),
                  'status': forms.HiddenInput(),
                  'winner': forms.HiddenInput()}


class CrispyTipping(forms.ModelForm):
    picks = forms.TypedChoiceField(
        label="picks",
        choices=(('hteam', 'hteam'), ('ateam', 'ateam')),
        widget=forms.RadioSelect(attrs={
        'class': 'form-check-inline'})
    )
    class Meta:
        model = tippings
        fields = ['first_name', 'last_name', 'email', 'fixture_id', 'picks', 
                  'margin', 'hteam', 'ateam', 'hteam_url', 'ateam_url', 'date', 
                  'venue', 'status', 'has_margin', 'winner', 'disabled']
        
    def __init__(self, *args, **kwargs):
        choices = (('hteam', 'hteam'), ('ateam', 'ateam'))
        super().__init__(*args, **kwargs)
        self.fields['first_name'].widget = HiddenInput()
        self.fields['last_name'].widget = HiddenInput()
        self.fields['email'].widget = HiddenInput()
        self.fields['hteam'].widget = HiddenInput()
        self.fields['ateam'].widget = HiddenInput()
        self.fields['hteam_url'].widget = HiddenInput()
        self.fields['ateam_url'].widget = HiddenInput()
        self.fields['date'].widget = HiddenInput()
        self.fields['venue'].widget = HiddenInput()
        self.fields['fixture_id'].widget = HiddenInput()
        self.fields['status'].widget = HiddenInput()
        self.fields['has_margin'].widget = HiddenInput()
        self.fields['picks'] = forms.ChoiceField(required=True, widget=forms.RadioSelect, choices=choices)
        self.fields['winner'].widget = HiddenInput()
        self.fields['disabled'].widget = HiddenInput()

        self.helper = FormHelper()
        self.helper.form_method = 'POST'
        self.helper.form_show_labels = False
        self.helper.layout = Layout(
            Div(InlineRadios('picks'), css_class="inline-block")
        )
