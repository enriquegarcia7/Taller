# Generated by Django 3.2.19 on 2023-06-24 02:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taller', '0003_trabajo_alter_reserva_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='trabajo',
            name='imagen',
            field=models.ImageField(null=True, upload_to='trabajos'),
        ),
    ]