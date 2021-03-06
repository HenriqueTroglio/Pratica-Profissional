# Generated by Django 2.2.4 on 2021-10-23 18:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FormaPagamento',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
                ('Descricao', models.CharField(max_length=50, verbose_name='Descrição')),
            ],
            options={
                'db_table': 'FormaPagamento',
            },
        ),
        migrations.CreateModel(
            name='Parcela',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
                ('Descricao', models.CharField(max_length=50, verbose_name='Descrição')),
                ('FormaPagamento', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='FormaPagamento_Parcela', to='Pagamentos.FormaPagamento')),
            ],
            options={
                'db_table': 'Parcela',
            },
        ),
        migrations.CreateModel(
            name='CondicaoPagamento',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
                ('Descricao', models.CharField(max_length=50, verbose_name='Descrição')),
                ('Juros', models.DecimalField(decimal_places=2, max_digits=20)),
                ('DataVencimento', models.DateField(verbose_name='Data de Vencimento')),
                ('DataRecebimento', models.DateField(verbose_name='Data de Recebimento')),
                ('Parcela', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='Parcela_CondicaoPagamento', to='Pagamentos.Parcela')),
            ],
            options={
                'db_table': 'CondicaoPagamento',
            },
        ),
    ]
