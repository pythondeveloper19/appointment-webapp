from django import forms

from .models import Appointments
import datetime
class MyModelForm(forms.ModelForm):

    class Meta:

        model = Appointments
        fields = ('datetime','description',)

        def clean_date(self):
            date = self.cleaned_data['datetime']
            if date < datetime.date.today():
                raise forms.ValidationError("The date cannot be in the past!")
            return date