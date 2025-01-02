
from datetime import timezone
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as loginDjango
from django.contrib.auth.decorators import login_required
from .models import Produto, Categoria, Fornecedor, MovimentacaoEstoque

def index(request):
    produtos = Produto.objects.all() 
    return render(request, 'index.html', {'produtos': produtos})

@login_required(login_url="/login/")
def sobre(request):
    pass


def contato(request):
    pass

def adicionar_produto(request):
    pass


#CRUD CATEGORIA ==================================================================================
def adicionar_categoria(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        descricao = request.POST.get('descricao')
        Categoria.objects.create(nome=nome, descricao=descricao)
        return redirect('index') 
    return render(request, 'categoria/adicionar_categoria.html')

def listar_categorias(request):
    categorias = Categoria.objects.all()
    return render(request, 'categoria/listar_categorias.html', {'categorias': categorias})

def editar_categoria(request, id):
    categoria = Categoria.objects.get(id=id)
    if request.method == 'POST':
        categoria.nome = request.POST.get('nome')
        categoria.descricao = request.POST.get('descricao')
        categoria.save()
        return redirect('listar_categorias')
    return render(request, 'categoria/editar_categoria.html', {'categoria': categoria})

def deletar_categoria(request, id):
    categoria = Categoria.objects.get(id=id)
    if request.method == 'POST':
        categoria.delete()
        return redirect('listar_categorias')
    return render(request, 'categoria/deletar_categoria.html', {'categoria': categoria})


#CRUD PRODUTO ==================================================================================
def adicionar_produto(request):
    categorias = Categoria.objects.all()
    if request.method == 'POST':
        nome = request.POST.get('nome')
        preco = request.POST.get('preco')
        quantidade = request.POST.get('quantidade')
        descricao = request.POST.get('descricao')
        id_categoria = request.POST.get('id_categoria')  
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

def editar_produto(request, id):
    produto = Produto.objects.get(id=id)
    if request.method == 'POST':
        produto.nome = request.POST.get('nome')
        produto.preco = request.POST.get('preco')
        produto.descricao = request.POST.get('descricao')
        categoria_id = request.POST.get('categoria_id')
        produto.categoria_id = Categoria.objects.get(id_categoria=categoria_id)
        produto.save()
        return redirect('index')
    return render(request, 'editar_produto.html', {'produto': produto})

def deletar_produto(request, id):
    produto = Produto.objects.get(id=id)
    if request.method == 'POST':
        produto.delete()
        return redirect('index')
    return render(request, 'deletar_produto.html', {'produto': produto})

#CRUD FORNECEDOR ==================================================================================
def adicionar_fornecedor(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        telefone = request.POST.get('telefone')
        email = request.POST.get('email')
        endereco = request.POST.get('endereco')

        Fornecedor.objects.create(
            nome=nome,
            telefone=telefone,
            email=email,
            endereco=endereco
        )
        return redirect('listar_fornecedores')
    return render(request, 'fornecedor/adicionar_fornecedor.html')

def listar_fornecedores(request):
    fornecedores = Fornecedor.objects.all()
    return render(request, 'fornecedor/listar_fornecedores.html', {'fornecedores': fornecedores})

def editar_fornecedor(request, id):
    fornecedor = Fornecedor.objects.get(id=id)
    if request.method == 'POST':
        fornecedor.nome = request.POST.get('nome')
        fornecedor.telefone = request.POST.get('telefone')
        fornecedor.email = request.POST.get('email')
        fornecedor.endereco = request.POST.get('endereco')
        fornecedor.save()
        return redirect('listar_fornecedores')
    return render(request, 'fornecedor/editar_fornecedor.html', {'fornecedor': fornecedor})

def deletar_fornecedor(request, id):
    fornecedor = Fornecedor.objects.get(id=id)
    if request.method == 'POST':
        fornecedor.delete()
        return redirect('listar_fornecedores')
    return render(request, 'fornecedor/deletar_fornecedor.html', {'fornecedor': fornecedor})

#CRUD MOVIMENTAÇÃO DO ESTOQUE ==================================================================================
def adicionar_movimentacao(request):
    produtos = Produto.objects.all()
    if request.method == 'POST':
        produto_id = request.POST.get('produto')
        tipo = request.POST.get('tipo')
        quantidade = int(request.POST.get('quantidade'))
        data_movimentacao = timezone.now()
        observacoes = request.POST.get('observacoes')

        
        if quantidade <= 0:
            return render(request, 'movimentacaoestoque/adicionar_movimentacao.html', {
                'produtos': produtos,
                'error': "A quantidade deve ser maior que zero."
            })

        MovimentacaoEstoque.objects.create(
            produto_id=produto_id,
            tipo=tipo,
            quantidade=quantidade,
            data_movimentacao=data_movimentacao,
            observacoes=observacoes
        )
        return redirect('listar_movimentacoes')
    return render(request, 'movimentacaoestoque/adicionar_movimentacao.html', {'produtos': produtos})

def listar_movimentacoes(request):
    movimentacoes = MovimentacaoEstoque.objects.select_related('produto').all()
    return render(request, 'movimentacaoestoque/listar_movimentacoes.html', {'movimentacoes': movimentacoes})

def editar_movimentacao(request, id):
    movimentacao = MovimentacaoEstoque.objects.get(id_movimentacao=id)
    produtos = Produto.objects.all()
    if request.method == 'POST':
        movimentacao.produto_id = request.POST.get('produto')
        movimentacao.tipo = request.POST.get('tipo')
        movimentacao.quantidade = int(request.POST.get('quantidade'))
        movimentacao.observacoes = request.POST.get('observacoes')
        movimentacao.save()
        return redirect('listar_movimentacoes')
    return render(request, 'movimentacaoestoque/editar_movimentacao.html', {
        'movimentacao': movimentacao,
        'produtos': produtos
    })

def deletar_movimentacao(request, id):
    movimentacao = MovimentacaoEstoque.objects.get(id_movimentacao=id)
    if request.method == 'POST':
        movimentacao.delete()
        return redirect('listar_movimentacoes')
    return render(request, 'movimentacaoestoque/deletar_movimentacao.html', {'movimentacao': movimentacao})


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



