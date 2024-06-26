# Generated by Django 4.2.5 on 2023-11-15 01:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lanche',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_vendedor', models.CharField(max_length=255)),
                ('produto_oferecido', models.CharField(max_length=255)),
                ('curso', models.CharField(max_length=255)),
                ('contato', models.CharField(max_length=20)),
                ('foto', models.ImageField(blank=True, null=True, upload_to='fotos/')),
            ],
        ),
    ]
