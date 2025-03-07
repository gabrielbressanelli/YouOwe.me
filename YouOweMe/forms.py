from django import forms
from  .models import DeadBeat, Debt

class DeadBeatForm(forms.ModelForm):
    class Meta:
        model = DeadBeat
        fields = ['debt', 'name', 'amount', 'date']

class DebtForm(forms.ModelForm):
    class Meta:
        model = Debt
        fields = ['name', 'purchase', 'total_amount', 'effective_date']
