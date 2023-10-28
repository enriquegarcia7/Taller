# Generated by Django 3.2.22 on 2023-10-27 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taller', '0012_producto'),
    ]

    operations = [
        migrations.CreateModel(
            name='Agenda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rut', models.CharField(max_length=10)),
                ('nombre', models.CharField(max_length=50)),
                ('telefono', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('detalle', models.CharField(max_length=2000)),
                ('fecha', models.DateField()),
            ],
        ),
    ]
