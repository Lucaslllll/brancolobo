from django import forms
from inicial.models import Doubt, Client
from .models import Product

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

class ProductForm(forms.ModelForm):
  class Meta:
    model = Product
    fields = '__all__'
    widgets = {
      'name': forms.TextInput(attrs={'class':'form-control', }),
      'price': forms.NumberInput(attrs={'class':'form-control'}),
      'ingredients': forms.SelectMultiple(attrs={'class':'form-control', 'required':False}),
      'image': forms.FileInput(attrs={'class':'form-control'}),
      'details': forms.Textarea(attrs={'class':'form-control'})
    }
    labels = {'name': "Nome", 'price': "Preço", 'ingredients': "Ingredientes",
    		  'image': "Imagem", 'details': "Detalhes",
    }
