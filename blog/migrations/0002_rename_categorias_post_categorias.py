# Generated by Django 4.1.7 on 2023-05-05 15:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='Categorias',
            new_name='categorias',
        ),
    ]
