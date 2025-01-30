from django.forms import ValidationError
from django.test import Client, TestCase
from django.urls import reverse
from estoque.models import Categoria, MovimentacaoEstoque, Produto, Fornecedor
from estoque.forms import ProdutoForm

class CategoriaTestCase(TestCase):
    def test_categoria_crud(self):
        # CREATE
        categoria = Categoria.objects.create(nome="Eletrônicos", descricao="Produtos eletrônicos")
        self.assertEqual(Categoria.objects.count(), 1)

        # READ
        categoria_lida = Categoria.objects.get(nome="Eletrônicos")
        self.assertEqual(categoria_lida.descricao, "Produtos eletrônicos")

        # UPDATE
        categoria_lida.nome = "Eletrodomésticos"
        categoria_lida.save()
        self.assertEqual(Categoria.objects.get(id_categoria=categoria.id_categoria).nome, "Eletrodomésticos")

        # DELETE
        categoria_lida.delete()
        self.assertEqual(Categoria.objects.count(), 0)


class FornecedorTestCase(TestCase):
    def test_fornecedor_crud(self):
        # CREATE
        fornecedor = Fornecedor.objects.create(
            nome="Tech Supplies Ltda",
            telefone="(87) 99999-9999",
            email="contato@techsupplies.com",
            endereco="Rua Principal, 123"
        )
        self.assertEqual(Fornecedor.objects.count(), 1)

        # READ
        fornecedor_lido = Fornecedor.objects.get(nome="Tech Supplies Ltda")
        self.assertEqual(fornecedor_lido.email, "contato@techsupplies.com")

        # UPDATE
        fornecedor_lido.telefone = "(87) 88888-8888"
        fornecedor_lido.save()
        self.assertEqual(Fornecedor.objects.get(id=fornecedor.id).telefone, "(87) 88888-8888")

        # DELETE
        fornecedor_lido.delete()
        self.assertEqual(Fornecedor.objects.count(), 0)


class ProdutoTestCase(TestCase):
    def test_produto_crud(self):
        # Criação de uma categoria para associar ao produto
        categoria = Categoria.objects.create(nome="Eletrônicos", descricao="Produtos eletrônicos")

        # Criação de um fornecedor para associar ao produto
        fornecedor = Fornecedor.objects.create(
            nome="Fornecedor A",
            telefone="(87) 99999-9999",
            email="fornecedorA@example.com",
            endereco="Rua dos Testes, 456"
        )

        # CREATE
        produto = Produto.objects.create(
            nome="Celular Galaxy",
            quantidade=10,
            preco=1999.99,
            categoria=categoria,
            descricao="Smartphone Samsung Galaxy"
        )
        produto.fornecedores.add(fornecedor)

        self.assertEqual(Produto.objects.count(), 1)

        # READ
        produto_lido = Produto.objects.get(nome="Celular Galaxy")
        self.assertEqual(produto_lido.descricao, "Smartphone Samsung Galaxy")
        self.assertEqual(produto_lido.categoria, categoria)
        self.assertIn(fornecedor, produto_lido.fornecedores.all())

        # UPDATE
        produto_lido.quantidade = 15
        produto_lido.save()
        self.assertEqual(Produto.objects.get(id_produto=produto.id_produto).quantidade, 15)

        # DELETE
        produto_lido.delete()
        self.assertEqual(Produto.objects.count(), 0)


class ViewsTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.categoria = Categoria.objects.create(nome="Eletrônicos", descricao="Produtos eletrônicos")
        self.fornecedor = Fornecedor.objects.create(
            nome="Fornecedor A",
            telefone="(87) 99999-9999",
            email="fornecedorA@example.com",
            endereco="Rua dos Testes, 456"
        )
        self.produto = Produto.objects.create(
            nome="Celular Galaxy",
            quantidade=10,
            preco=1999.99,
            categoria=self.categoria,
            descricao="Smartphone Samsung Galaxy"
        )
        self.produto.fornecedores.add(self.fornecedor)

    def test_categoria_list_view(self):
        response = self.client.get(reverse('listar_categorias'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Eletrônicos")

    def test_produto_list_view(self):
        response = self.client.get(reverse('listar_produtos'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Celular Galaxy")

    def test_fornecedor_list_view(self):
        response = self.client.get(reverse('listar_fornecedores'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Fornecedor A")


class ModelTestCase(TestCase):
    def setUp(self):
        self.categoria = Categoria.objects.create(nome="Eletrônicos", descricao="Produtos eletrônicos")
        self.produto = Produto.objects.create(
            nome="Notebook Dell",
            quantidade=5,
            preco=3500.00,
            categoria=self.categoria,
            descricao="Notebook de alto desempenho"
        )

    def test_movimentacao_estoque_quantidade_invalida(self):
        """Testa se a validação impede movimentações com quantidade zero ou negativa"""
        movimentacao = MovimentacaoEstoque(
            produto=self.produto,
            tipo="entrada",
            quantidade=0
        )
        with self.assertRaises(ValidationError):
            movimentacao.full_clean()  # Deve lançar um erro de validação

class ProdutoFormTest(TestCase):
    def test_produto_form_valido(self):
        # Criar instâncias de Categoria e Fornecedor antes de testar o formulário
        categoria = Categoria.objects.create(nome="Eletrônicos", descricao="Produtos eletrônicos")
        fornecedor = Fornecedor.objects.create(
            nome="Fornecedor A",
            telefone="(87) 99999-9999",
            email="fornecedorA@example.com",
            endereco="Rua dos Testes, 456"
        )

        # Dados do formulário com fornecedor incluso
        form_data = {
            'nome': 'Celular Galaxy',
            'quantidade': 10,
            'preco': '1999.99',  
            'descricao': 'Smartphone Samsung Galaxy',
            'categoria': categoria.id_categoria,
            'fornecedores': [fornecedor.id]  # Lista de IDs para ManyToManyField
        }
        
        form = ProdutoForm(data=form_data)
        self.assertTrue(form.is_valid())  # Deve passar agora
