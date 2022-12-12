from django import forms
from oficina.models import *


class ClienteForms(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'
        
        widgets = {
            'status_pag': forms.RadioSelect()
        }
        
class ProdutoForms(forms.ModelForm):
    class Meta:
        model = Produto
        fields = '__all__'
        
class ServicoForms(forms.ModelForm):
    class Meta:
        model = Servico
        fields = '__all__'
