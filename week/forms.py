from django import forms


# Customize default DateInput django widget to make date input field
class DateInput(forms.DateInput):
    input_type = 'date'


class DateForm(forms.Form):
    date = forms.DateField(label='Дата', widget=DateInput(attrs={
        'class': 'form-control form-control-lg'
    }))
