# Generated by Django 2.2.3 on 2019-07-31 00:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('endereco', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pais',
            options={'verbose_name': 'País', 'verbose_name_plural': 'Paises'},
        ),
        migrations.AddField(
            model_name='pais',
            name='ativo',
            field=models.BooleanField(default=True),
        ),
    ]
