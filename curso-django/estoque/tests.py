from django.test import TestCase
from estoque.models import Categoria
# Create your tests here.
class CategoriaTestCase(TestCase):
    def test_categoria_creation(self):
        categoria = Categoria.objects.create(nome="Teste", descricao="Descrição de teste")
        self.assertEqual(Categoria.objects.count(), 1)