# Generated by Django 5.2 on 2025-04-25 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('quantite', models.IntegerField()),
                ('prix_unitaire', models.DecimalField(decimal_places=2, max_digits=10)),
                ('date_ajout', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
