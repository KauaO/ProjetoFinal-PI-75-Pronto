import django_filters
from oficina.models import *

class ProdutoFilter(django_filters.FilterSet):
     
     class Meta:
         model = Produto
         fields = {'categoria': ['exact'], 'valor_produto': ['icontains']}


class MarcaFilter(django_filters.FilterSet):

        class Meta:
            model = Marca
            fields = {'nome': ['icontains']}