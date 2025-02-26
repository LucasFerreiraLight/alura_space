from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.

class Fotografia(models.Model):
    # Nome caractheres ou seja String
    #exemplo null x = (nada) --- blank >> x = ""

    opcoes_de_categoria = [
        {"NEBULOSA", "Nebula"},
        {"ESTRELA", "Star"},
        {"GALÁXIA", "Galaxy"},
        {"PLANETA", "Planet"}
    ]

    nome = models.CharField(max_length=100, null=False, blank=False)
    legenda = models.CharField(max_length=150, null=False, blank=False)
    categoria = models.CharField(max_length=100, choices=opcoes_de_categoria, default='')
    descricao = models.TextField(null=False, blank=False)
    
    #ALTERADO DE:
    #foto = models.CharField(max_length=100, null=False, blank=False)
    #PARA 
    foto = models.ImageField(upload_to="fotos/%Y/%m/%d", blank=True)

    publicada = models.BooleanField(default=False)
    data_fotografia = models.DateTimeField(default=datetime.now, blank=False)

    usuario = models.ForeignKey(
        to=User,
        on_delete=models.SET_NULL,
        null=True,
        blank=False,
        related_name="user",
        
    )




    def __str__(self):
        return self.nome
    
    


