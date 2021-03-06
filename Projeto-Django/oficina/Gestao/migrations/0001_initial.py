# Generated by Django 2.2.4 on 2021-10-23 15:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Pessoas', '0005_auto_20210925_1443'),
        ('Produtos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ItemVenda',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Quantidade', models.IntegerField()),
                ('ValorTotal', models.DecimalField(decimal_places=2, max_digits=20, verbose_name='Valor Total')),
                ('ValorUnitario', models.DecimalField(decimal_places=2, max_digits=20, verbose_name='Valor Unitário')),
                ('Produto', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Produtos.Produto')),
            ],
        ),
        migrations.CreateModel(
            name='Venda',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NumeroNota', models.CharField(max_length=50, verbose_name='Número da Nota')),
                ('SerieNota', models.CharField(max_length=50, verbose_name='Série da Nota')),
                ('ModeloNota', models.CharField(max_length=50, verbose_name='Modelo da Nota')),
                ('Cliente', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='Venda_Cliente', to='Pessoas.Cliente')),
                ('Produtos', models.ManyToManyField(through='Gestao.ItemVenda', to='Produtos.Produto')),
            ],
            options={
                'db_table': 'Venda',
                'unique_together': {('NumeroNota', 'SerieNota', 'ModeloNota')},
            },
        ),
        migrations.AddField(
            model_name='itemvenda',
            name='Venda',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Gestao.Venda'),
        ),
    ]
