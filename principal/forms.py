from django import forms
from inicial.models import Doubt, Client

class DoubtForm(forms.ModelForm):
  class Meta:
    model = Doubt
    fields = '__all__'
    widgets = {
      'ask': forms.TextInput(attrs={'class':'form-control', }),
      'response': forms.Textarea(attrs={'class':'form-control'}),
      
    }
    labels = {'ask': "Pergunta",
    		  'response': "Resposta",
    }


class ClientForm(forms.ModelForm):
  class Meta:
    model = Client
    fields = '__all__'
    widgets = {
      'name': forms.TextInput(attrs={'class':'form-control', }),
      'details': forms.Textarea(attrs={'class':'form-control'}),
      
    }
    labels = {'name': "Nome",
    		  'details': "Detalhes",
    }
