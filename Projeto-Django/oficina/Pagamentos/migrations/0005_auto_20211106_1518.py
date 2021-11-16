# Generated by Django 2.2.4 on 2021-11-06 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pagamentos', '0004_parcela_numero'),
    ]

    operations = [
        migrations.AddField(
            model_name='parcela',
            name='Percentual',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=20, verbose_name='Percentual'),
        ),
        migrations.AlterField(
            model_name='parcela',
            name='Numero',
            field=models.IntegerField(verbose_name='Número'),
        ),
        migrations.AlterUniqueTogether(
            name='parcela',
            unique_together={('Numero', 'CondicaoPagamento')},
        ),
        migrations.RemoveField(
            model_name='parcela',
            name='Descricao',
        ),
    ]
