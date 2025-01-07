from django.db import models
from django.forms import ValidationError
from django.utils import timezone

class Categoria(models.Model):
    id_categoria = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=250)
    descricao = models.CharField(max_length=255)
    def __str__(self):
        return self.nome  

class Produto(models.Model):
    id_produto = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    quantidade = models.IntegerField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.ForeignKey(
        'estoque.Categoria', 
        on_delete=models.CASCADE, 
        null=True,  
        blank=True  
    )
    descricao = models.TextField(default="")
    fornecedores = models.ManyToManyField('estoque.Fornecedor', related_name="produtos")
    def __str__(self):
        return self.nome

class MovimentacaoEstoque(models.Model):
    id_movimentacao = models.AutoField(primary_key=True, default=0)
    produto = models.ForeignKey('estoque.Produto', on_delete=models.CASCADE)
    tipo = models.CharField(max_length=20, choices=[('entrada', 'Entrada'), ('saida', 'Saída')])
    quantidade = models.IntegerField()
    data_movimentacao = models.DateTimeField(default=timezone.now) 
    observacoes = models.TextField(blank=True, null=True)

    def clean(self):
        if self.quantidade <= 0:
            raise ValidationError("A quantidade deve ser maior que zero.")
class Fornecedor(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=15)
    email = models.EmailField(max_length=255)
    endereco = models.CharField(max_length=200)
    def __str__(self):
        return self.nome
    
    
