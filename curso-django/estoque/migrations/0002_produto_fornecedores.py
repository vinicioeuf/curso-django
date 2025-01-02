# Generated by Django 5.1.4 on 2025-01-02 22:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estoque', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='fornecedores',
            field=models.ManyToManyField(related_name='produtos', to='estoque.fornecedor'),
        ),
    ]
