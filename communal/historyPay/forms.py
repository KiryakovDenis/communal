from django import forms

class RenderPeriodForm(forms.Form):
    name = forms.CharField(max_length=50, help_text="Наименование периода")
    begin_d = forms.DateField(help_text='Дата начала периода')
    end_d   = forms.DateField(help_text='Дата окончанияе периода')
    comment = forms.TextField(max_length=500, help_text='Примечание', blank=True, null=True)