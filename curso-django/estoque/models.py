from django.db import models

# Create your models here.
class Produto(models.Model):
    nome = models.CharField(max_length=100)
    quantidade =models.IntegerField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)