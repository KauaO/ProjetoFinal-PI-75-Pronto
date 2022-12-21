"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from oficina.views import *
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Index, name="index.html"),
    path("pneus/", Pneus, name="pneus.html"),
    path("aros/", Aros, name="aros.html"),
    path("raios/", Raios, name="raios.html"),
    path("farois/", Farois, name="farois.html"),
    path("retrovisores/", Retrovisores, name="retrovisores.html"),
    path("atendimento/", Atendimento, name="atendimento.html"),
    path("cadastro_servico/", cadastrar_servico, name="form_servico.html"),
    path('cadastro_cliente/', cadastrar_cliente, name="form_cliente.html"),
    path('cadastro_produto/', cadastrar_produto, name="form_produto.html"),
    path('teste/', teste, name="teste.html") 

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
