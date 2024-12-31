
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as loginDjango
from django.contrib.auth.decorators import login_required
from .models import Produto, Categoria

def index(request):
    produtos = Produto.objects.all()  # Busca todos os registros da tabela Produto
    return render(request, 'index.html', {'produtos': produtos})

@login_required(login_url="/login/")
def sobre(request):
    pass


def contato(request):
    pass

def adicionar_produto(request):
    pass



def adicionar_categoria(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        descricao = request.POST.get('descricao')
        Categoria.objects.create(nome=nome, descricao=descricao)
        return redirect('index')  # Redirecionar para a lista de categorias
    return render(request, 'categoria/adicionar_categoria.html')

def listar_categorias(request):
    categorias = Categoria.objects.all()
    return render(request, 'listar_categorias.html', {'categorias': categorias})

def editar_categoria(request, id):
    categoria = Categoria.objects.get(id=id)
    if request.method == 'POST':
        categoria.nome = request.POST.get('nome')
        categoria.descricao = request.POST.get('descricao')
        categoria.save()
        return redirect('listar_categorias')
    return render(request, 'editar_categoria.html', {'categoria': categoria})

def deletar_categoria(request, id):
    categoria = Categoria.objects.get(id=id)
    if request.method == 'POST':
        categoria.delete()
        return redirect('listar_categorias')
    return render(request, 'deletar_categoria.html', {'categoria': categoria})

def adicionar_produto(request):
    categorias = Categoria.objects.all()
    if request.method == 'POST':
        nome = request.POST.get('nome')
        preco = request.POST.get('preco')
        quantidade = request.POST.get('quantidade')
        descricao = request.POST.get('descricao')
        id_categoria = request.POST.get('id_categoria')  # Certifique-se de que o nome seja consistente
        categoria = Categoria.objects.get(id_categoria=id_categoria)
        
        Produto.objects.create(
            nome=nome,
            preco=preco,
            quantidade=quantidade,
            descricao=descricao,
            categoria=categoria
        )
        return redirect('index')
    return render(request, 'produto/adicionar_produto.html', {'categorias': categorias})

def listar_produtos(request):
    produtos = Produto.objects.select_related('categoria').all()
    return render(request, 'produto/listar_produtos.html', {'produtos': produtos})


def cadastro(request):
    if request.method == 'GET':
        return render(request, 'autenticacao/cadastro.html')
    else:
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        user = User.objects.filter(email=email).first()
        if user:
            return HttpResponse('Já existe um usuário com este e-mail.')
       
        novo_usuario = User.objects.create_user(email=email, password=senha, first_name=nome, username=email)
        novo_usuario.save()

        return redirect('/login')


def login(request):
    if request.method == 'GET':
        return render(request, 'autenticacao/login.html')
    else:
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        user = authenticate(username=email, password=senha)

        if user:
            loginDjango(request, user)
            return redirect('index')
        else:
            return HttpResponse('E-mail ou senha inválidas')
        
def logout_view(request):
    logout(request)



