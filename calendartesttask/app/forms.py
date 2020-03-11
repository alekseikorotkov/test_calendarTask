from db.models import Agreement
from django import forms
from django.core.exceptions import ValidationError

class AgreementForm(forms.ModelForm):
    class Meta:
            model = Agreement
            fields = '__all__'


    def clean(self):
        list_selected = self.cleaned_data.get('period')
        if not list_selected:
            raise ValidationError(
                    ('You don\'t choise periods'))

        max_period_date = min(list_selected, key= lambda y:y.stop).stop
        min_period_date = max(list_selected, key= lambda y:y.start).start

        if min_period_date < self.cleaned_data.get('start') or max_period_date > self.cleaned_data.get('stop'):
            raise ValidationError(('dates of period is not corrent'))

        for i in range(len(list_selected)):
            for j in range(i+1,len(list_selected)):
                if list_selected[i].start < list_selected[j].start < list_selected[i].stop:
                    raise ValidationError(('date of periods is across'))

        return self.cleaned_data