# Generated by Django 4.2.7 on 2023-11-15 00:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0013_alter_project_nbrlotstotal_alter_stock_nomproject'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='idBienDemande',
        ),
    ]
