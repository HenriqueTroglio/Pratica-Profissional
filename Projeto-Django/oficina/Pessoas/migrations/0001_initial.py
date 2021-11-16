# Generated by Django 2.2.4 on 2021-09-18 07:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('endereco', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
                ('Nome', models.CharField(max_length=50)),
                ('CPF', models.CharField(max_length=50)),
                ('RG', models.CharField(max_length=30)),
                ('DataNascimento', models.DateField()),
                ('Email', models.CharField(max_length=50)),
                ('Telefone', models.CharField(max_length=30)),
                ('Logradouro', models.CharField(max_length=100)),
                ('Bairro', models.CharField(max_length=50)),
                ('CEP', models.CharField(max_length=20)),
                ('Numero', models.CharField(max_length=20)),
                ('Complemento', models.CharField(max_length=100)),
                ('Cidade', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='Cidade', to='endereco.Cidade')),
            ],
            options={
                'db_table': 'Cliente',
            },
        ),
    ]