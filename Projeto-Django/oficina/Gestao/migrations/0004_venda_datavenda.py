# Generated by Django 2.2.4 on 2021-11-15 22:44

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Gestao', '0003_auto_20211115_1452'),
    ]

    operations = [
        migrations.AddField(
            model_name='venda',
            name='DataVenda',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Data da Venda'),
        ),
    ]
