
from django.utils import timezone
from django.http import HttpResponse
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as loginDjango
from django.contrib.auth.decorators import login_required
from .models import Produto, Categoria, Fornecedor, MovimentacaoEstoque
from .forms import ProdutoForm, CategoriaForm, FornecedorForm, MovimentacaoEstoqueForm

#Caso dê algum problema no arquivo zipado, aqui está o link do repositório no github: https://github.com/vinicioeuf/curso-django
@login_required(login_url="/login/")
def index(request):
    produtos = Produto.objects.all() 
    fornecedores = Fornecedor.objects.all()
    return render(request, 'index.html', {'produtos': produtos, 'fornecedores': fornecedores})


@login_required(login_url="/login/")
def sobre(request):
    pass

@login_required(login_url="/login/")
def contato(request):
    pass
@login_required(login_url="/login/")
def adicionar_produto(request):
    pass


#CRUD CATEGORIA ==================================================================================
def adicionar_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()  
            return redirect('index')
    else:
        form = CategoriaForm() 
    
    return render(request, 'categoria/adicionar_categoria.html', {'form': form})

def listar_categorias(request):
    categorias = Categoria.objects.all() 
    return render(request, 'categoria/listar_categorias.html', {'categorias': categorias})

def editar_categoria(request, id_categoria):
    categoria = get_object_or_404(Categoria, id_categoria=id_categoria)
    
    if request.method == 'POST':
        form = CategoriaForm(request.POST, instance=categoria)
        if form.is_valid():
            form.save()
            return redirect('listar_categorias')
    else:
        form = CategoriaForm(instance=categoria)
    
    return render(request, 'categoria/editar_categoria.html', {
        'form': form,
        'categoria': categoria
    })

    
def deletar_categoria(request, id_categoria):
    categoria = get_object_or_404(Categoria, id_categoria=id_categoria)
    
    if request.method == 'POST':
        categoria.delete() 
        return redirect('listar_categorias')
    
    return render(request, 'categoria/deletar_categoria.html', {'categoria': categoria})
#CRUD PRODUTO ==================================================================================

def adicionar_produto(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()  
            return redirect('index')
    else:
        form = ProdutoForm()  
    
    return render(request, 'produto/adicionar_produto.html', {'form': form})

def listar_produtos(request):
    produtos = Produto.objects.select_related('categoria').prefetch_related('fornecedores').all()
    return render(request, 'produto/listar_produtos.html', {'produtos': produtos})

def editar_produto(request, id_produto):
    produto = get_object_or_404(Produto, id_produto=id_produto)
    
    if request.method == 'POST':
        form = ProdutoForm(request.POST, instance=produto)
        if form.is_valid():
            form.save()
            return redirect('listar_produtos')
    else:
        form = ProdutoForm(instance=produto)
    
    return render(request, 'produto/editar_produto.html', {'form': form, 'produto': produto})

def deletar_produto(request, id_produto):
    produto = get_object_or_404(Produto, id_produto=id_produto)
    
    if request.method == 'POST':
        produto.delete() 
        return redirect('listar_produtos')
    
    return render(request, 'produto/deletar_produto.html', {'produto': produto})
#CRUD FORNECEDOR ==================================================================================
def adicionar_fornecedor(request):
    if request.method == 'POST':
        form = FornecedorForm(request.POST)
        if form.is_valid():
            form.save()  
            return redirect('index')
    else:
        form = FornecedorForm() 
    
    return render(request, 'fornecedor/adicionar_fornecedor.html', {'form': form})

def listar_fornecedores(request):
    fornecedores = Fornecedor.objects.all()
    return render(request, 'fornecedor/listar_fornecedores.html', {'fornecedores': fornecedores})

# Editar Fornecedor
def editar_fornecedor(request, id):
    fornecedor = get_object_or_404(Fornecedor, id=id)

    if request.method == 'POST':
        form = FornecedorForm(request.POST, instance=fornecedor)
        if form.is_valid():
            form.save()
            return redirect('listar_fornecedores')
    else:
        form = FornecedorForm(instance=fornecedor)

    return render(request, 'fornecedor/editar_fornecedor.html', {
        'form': form,
        'fornecedor': fornecedor
    })

# Deletar Fornecedor
def deletar_fornecedor(request, id):
    fornecedor = get_object_or_404(Fornecedor, id=id)

    if request.method == 'POST':
        fornecedor.delete()
        return redirect('listar_fornecedores')

    return render(request, 'fornecedor/deletar_fornecedor.html', {'fornecedor': fornecedor})
#CRUD MOVIMENTAÇÃO DO ESTOQUE ==================================================================================
def adicionar_movimentacao(request):
    if request.method == 'POST':
        form = MovimentacaoEstoqueForm(request.POST)
        if form.is_valid():
            movimentacao = form.save(commit=False)
            movimentacao.save() 
            return redirect('listar_movimentacoes')
    else:
        form = MovimentacaoEstoqueForm()
    
    return render(request, 'movimentacaoestoque/adicionar_movimentacao.html', {'form': form})


def listar_movimentacoes(request):
    movimentacoes = MovimentacaoEstoque.objects.select_related('produto').all()
    return render(request, 'movimentacaoestoque/listar_movimentacoes.html', {'movimentacoes': movimentacoes})

def editar_movimentacao(request, id):
    movimentacao = get_object_or_404(MovimentacaoEstoque, id_movimentacao=id)
    
    if request.method == 'POST':
        form = MovimentacaoEstoqueForm(request.POST, instance=movimentacao)
        if form.is_valid():
            form.save()
            return redirect('listar_movimentacoes')
    else:
        form = MovimentacaoEstoqueForm(instance=movimentacao)
    
    return render(request, 'movimentacaoestoque/editar_movimentacao.html', {
        'form': form,
        'movimentacao': movimentacao
    })
    
def deletar_movimentacao(request, id):
    movimentacao = get_object_or_404(MovimentacaoEstoque, id_movimentacao=id)
    
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
    return redirect('login')
