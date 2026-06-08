from django.db import models

class Carro(models.Model):
    OPCOES_SITUACOES = [
        ('disponivel', 'Disponivel'), 
        ('reservado', 'Reservado'), 
        ('vendido', 'Vendido'),
    ]

    marca = models.CharField(max_length=200)
    modelo = models.CharField(max_length=200)
    ano = models.IntegerField()
    situacao = models.CharField(
        max_length=20,
        choices=OPCOES_SITUACOES,
        default='disponivel'
    )

    def __str__(self):
        return self.modelo