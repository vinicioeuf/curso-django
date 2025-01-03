from django.test import TestCase
from estoque.models import Categoria, Produto, Fornecedor
# Create your tests here.
class CategoriaTestCase(TestCase):
    def test_categoria_creation(self):
        categoria = Categoria.objects.create(nome="Teste", descricao="Descrição de teste")
        self.assertEqual(Categoria.objects.count(), 1)

class ProdutoTestCase(TestCase):
    def test_produto_creation(self):
        # Criação de uma categoria para associar ao produto
        categoria = Categoria.objects.create(nome="Eletrônicos", descricao="Produtos eletrônicos")
        
        # Criação de um fornecedor para associar ao produto
        fornecedor = Fornecedor.objects.create(
            nome="Tech Supplies Ltda",
            telefone="(87) 99999-9999",
            email="contato@techsupplies.com",
            endereco="Rua Principal, 123"
        )
        
        # Criação do produto
        produto = Produto.objects.create(
            nome="Notebook IdeaPad 3i",
            quantidade=5,
            preco=2799.00,
            categoria=categoria,
            descricao="Notebook muito bom bla bla"
        )
        
        # Associando o fornecedor ao produto (Many-to-Many)
        produto.fornecedores.add(fornecedor)
        
        # Verificações
        self.assertEqual(Produto.objects.count(), 1)
        self.assertEqual(produto.nome, "Notebook IdeaPad 3i")
        self.assertEqual(produto.categoria, categoria)
        self.assertIn(fornecedor, produto.fornecedores.all())