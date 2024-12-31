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
    # path('produtos/', views.listar_produtos, name='listar_produtos'),
    path('reset_password/', auth_views.PasswordResetView.as_view(), name="reset_password"),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"),
    path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete")
]