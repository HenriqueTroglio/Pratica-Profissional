# Generated by Django 2.2.4 on 2021-09-25 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pessoas', '0004_auto_20210918_0515'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cargo',
            name='Descricao',
            field=models.CharField(max_length=100, verbose_name='Descrição'),
        ),
        migrations.AlterField(
            model_name='cargo',
            name='Salario',
            field=models.DecimalField(decimal_places=2, max_digits=20, verbose_name='Salário'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='DataNascimento',
            field=models.DateField(verbose_name='Data de Nascimento'),
        ),
    ]