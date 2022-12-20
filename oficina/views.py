from django.shortcuts import render
from main.forms import *
from oficina.models import *

# Create your views here.

def Index(request):
    lista_produtos = Produto.objects.all()
    context = {'produtos' : lista_produtos}
    return render (request, 'index.html', context)  

def cadastrar_cliente(request):
    if request.method == 'POST':
        form_cliente = ClienteForms(request.POST)
        if form_cliente.is_valid():
            form_cliente.save()
            form_cliente = ClienteForms()
    else:
        form_cliente = ClienteForms()
    
    return render (request,"form_cliente.html", {'form_cliente' : form_cliente }) 

def cadastrar_produto(request):
    if str(request.method) == 'POST':
        form_produto = ProdutoForms(request.POST, request.FILES)
        if form_produto.is_valid():
            form_produto.save()
            form_produto = ProdutoForms()
    else:
        form_produto = ProdutoForms()
    
    return render (request,"form_produto.html", {'form_produto' : form_produto })

def cadastrar_servico(request):
    if request.method == 'POST':
        form_servico = ServicoForms(request.POST)
        if form_servico.is_valid():
            form_servico.save()
            form_servico = ServicoForms()
    else:
        form_servico = ServicoForms()
    
    return render (request,"form_servico.html", {'form_servico' : form_servico })

def Pneus(request):
    lista_pneus = Produto.objects.all()
    return render (request, "pneus.html", {'pneus' : lista_pneus})

def Aros(request):
    lista_aros = Produto.objects.all()
    return render (request, "aros.html", {'aros' : lista_aros})

def Raios(request):
    lista_raios = Produto.objects.all()
    return render (request, "raios.html", {'raios' : lista_raios})

def Farois(request):
    lista_farois = Produto.objects.all()
    return render (request, "farois.html", {'farois' : lista_farois})

def Retrovisores(request):
    lista_retrovisores = Produto.objects.all()
    return render (request, "retrovisores.html", {'pneus' : lista_retrovisores})

def Atendimento(request):
    return render (request, "atendimento.html")