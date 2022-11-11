from django import forms
from .models import Aluno

GENDER = [
  ("Masculino", "Masculino"),
  ("Feminino", "Feminino"),
  ("Outro 1", "Outro 1"),
  ("Outro 2", "Outro 2"),
  ("Outro 3", "Outro 3"),
]

class AlunoForm(forms.ModelForm):

  # Agora ta tudo OK, só mudar os nomes ai dos campus
  gender = forms.MultipleChoiceField(choices=GENDER, widget=forms.CheckboxSelectMultiple())
    
  discipline = forms.ChoiceField(choices=Aluno.discipline.field.choices, widget=forms.RadioSelect())

  class Meta:
    model = Aluno
    fields = ['name', 'gender', 'discipline']

