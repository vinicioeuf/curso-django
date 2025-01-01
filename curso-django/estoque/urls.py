from . import views
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('index', views.index, name='index'),
    path('cadastro', views.cadastro, name='cadastro'),
    path('login/', views.login, name='login'),
    path('sobre', views.sobre, name="sobre"),
    path('contato', views.contato, name="contato"),
    path('adicionar_produto', views.adicionar_produto, name="adicionar_produto"),
    path('adicionar_categoria', views.adicionar_categoria, name="adicionar_categoria"),
    path('categorias/editar/<int:id>/', views.editar_categoria, name='editar_categoria'),
    path('categorias/deletar/<int:id>/', views.deletar_categoria, name='deletar_categoria'),
    path('categorias/', views.listar_categorias, name='listar_categorias'),
    path('produtos/', views.listar_produtos, name='listar_produtos'),
    
    path('produtos/adicionar/', views.adicionar_produto, name='adicionar_produto'),
    path('produtos/editar/<int:id>/', views.editar_produto, name='editar_produto'),
    path('produtos/deletar/<int:id>/', views.deletar_produto, name='deletar_produto'),
    
    # URLs para Movimentação de Estoque
    path('movimentacoes/', views.listar_movimentacoes, name='listar_movimentacoes'),
    path('movimentacoes/adicionar/', views.adicionar_movimentacao, name='adicionar_movimentacao'),
    path('movimentacoes/editar/<int:id>/', views.editar_movimentacao, name='editar_movimentacao'),
    path('movimentacoes/deletar/<int:id>/', views.deletar_movimentacao, name='deletar_movimentacao'),

    # URLs para Fornecedor
    path('fornecedor/', views.listar_fornecedores, name='listar_fornecedores'),
    path('fornecedor/adicionar/', views.adicionar_fornecedor, name='adicionar_fornecedor'),
    path('fornecedor/editar/<int:id>/', views.editar_fornecedor, name='editar_fornecedor'),
    path('fornecedor/deletar/<int:id>/', views.deletar_fornecedor, name='deletar_fornecedor'),
    
    #URLs resetar senha
    path('reset_password/', auth_views.PasswordResetView.as_view(), name="reset_password"),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"),
    path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete")
]
