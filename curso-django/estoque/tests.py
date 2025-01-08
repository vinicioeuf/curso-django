from django.test import TestCase
from estoque.models import Categoria, Produto, Fornecedor

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
