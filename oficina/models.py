from tkinter.tix import Tree
from django.db import models

# Create your models here.

STATUS= [   
    ('Sim', 'Sim'),
    ('Não',  'Não')
]

class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    
    def __str__(self) -> str:
        return self.nome

class Marca(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.nome
    
class Produto(models.Model):
    perfil = models.IntegerField(blank=True, null=True)
    tamanho = models.IntegerField(blank=True, null=True)
    tipo = models.CharField(max_length=100, blank=True, null=True)
    largura = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    material = models.CharField(max_length=100, blank=True, null=True)
    cor = models.CharField(max_length=100, blank=True, null=True)
    valor_produto = models.DecimalField('Valor do produto', max_digits=5, decimal_places=2)
    quantidade = models.IntegerField()
    imagem = models.ImageField(upload_to='media/', blank=True, null=True, max_length=250) 
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    
   
class Servico(models.Model):
    descricao = models.TextField()
    placa = models.CharField(max_length=50)
    valor_servico = models.IntegerField()
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    
class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    CPF = models.CharField(max_length=100)
    telefone = models.CharField(max_length=100)
    status_pag = models.CharField(max_length=100, choices=STATUS, blank=True, null=True)
    saldo = models.IntegerField(blank=True, null=True)
    servico = models.ManyToManyField(Servico, blank=True, null=True)

    def __str__(self) -> str:
        return self.nome
    
class Atendimento(models.Model):
    valor_total = models.DecimalField('Valor total', max_digits=5, decimal_places=2, null=True)
    servico = models.OneToOneField(Servico, on_delete=models.CASCADE)
    