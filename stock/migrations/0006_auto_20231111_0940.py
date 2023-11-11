# Generated by Django 3.2.4 on 2023-11-11 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0005_remove_addtask_price_per_item'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='name',
            new_name='nom',
        ),
        migrations.RenameField(
            model_name='stock',
            old_name='apartement',
            new_name='bloc',
        ),
        migrations.RenameField(
            model_name='stock',
            old_name='block',
            new_name='cote',
        ),
        migrations.RenameField(
            model_name='stock',
            old_name='date',
            new_name='dateReservation',
        ),
        migrations.RenameField(
            model_name='stock',
            old_name='created_by',
            new_name='nomProject',
        ),
        migrations.RenameField(
            model_name='stock',
            old_name='issued_by',
            new_name='numBien',
        ),
        migrations.RenameField(
            model_name='stock',
            old_name='issued_to',
            new_name='numLOT',
        ),
        migrations.RenameField(
            model_name='stock',
            old_name='issue_quantity',
            new_name='prixM2HorsTaxe',
        ),
        migrations.RenameField(
            model_name='stock',
            old_name='quantity',
            new_name='superficieHabitable',
        ),
        migrations.RenameField(
            model_name='stock',
            old_name='item_name',
            new_name='vue',
        ),
        migrations.RemoveField(
            model_name='person',
            name='city',
        ),
        migrations.RemoveField(
            model_name='person',
            name='country',
        ),
        migrations.RemoveField(
            model_name='person',
            name='name',
        ),
        migrations.RemoveField(
            model_name='person',
            name='state',
        ),
        migrations.RemoveField(
            model_name='person',
            name='user',
        ),
        migrations.RemoveField(
            model_name='project',
            name='city',
        ),
        migrations.RemoveField(
            model_name='project',
            name='country',
        ),
        migrations.RemoveField(
            model_name='project',
            name='end_date',
        ),
        migrations.RemoveField(
            model_name='project',
            name='start_date',
        ),
        migrations.RemoveField(
            model_name='project',
            name='state',
        ),
        migrations.RemoveField(
            model_name='stock',
            name='Code_Bar',
        ),
        migrations.RemoveField(
            model_name='stock',
            name='category',
        ),
        migrations.RemoveField(
            model_name='stock',
            name='image',
        ),
        migrations.RemoveField(
            model_name='stock',
            name='last_updated',
        ),
        migrations.RemoveField(
            model_name='stock',
            name='price',
        ),
        migrations.RemoveField(
            model_name='stock',
            name='project',
        ),
        migrations.RemoveField(
            model_name='stock',
            name='re_order',
        ),
        migrations.RemoveField(
            model_name='stock',
            name='receive_quantity',
        ),
        migrations.RemoveField(
            model_name='stock',
            name='received_by',
        ),
        migrations.RemoveField(
            model_name='stock',
            name='timestamp',
        ),
        migrations.AddField(
            model_name='person',
            name='dateDossier',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='person',
            name='dateNaissance',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='person',
            name='idBienDemande',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='person',
            name='idIdentite',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='person',
            name='lieuNaissance',
            field=models.CharField(blank=True, default='', max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='person',
            name='nom',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='person',
            name='nomDossier',
            field=models.CharField(blank=True, default='', max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='Localisation',
            field=models.CharField(default=1, max_length=150),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='Observation',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='nbILOT',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='nbrLotsTotal',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='type',
            field=models.CharField(choices=[('Promotionnel', 'Promotionnel'), ('LOT Terrin', 'LOT Terrin')], default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='stock',
            name='Observatioin',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='stock',
            name='etat',
            field=models.CharField(choices=[('Libre', 'Libre'), (' Réservé', 'Réservé'), (' Vendu', 'Vendu')], default='1', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='stock',
            name='montantHorsTaxe',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='stock',
            name='montantTTC',
            field=models.IntegerField(default='1'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='stock',
            name='montantVenteTotal',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='stock',
            name='prixM2TTC',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='stock',
            name='prixVenteM2',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='stock',
            name='superficieUtil',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='stock',
            name='typeBien',
            field=models.CharField(choices=[('Appartement F3', 'Appartement F3'), ('Appartement F4', 'Appartement F4'), ('Appartement F5', 'Appartement F5'), ('Service', 'Service'), ('Local', 'Local')], default='1', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='person',
            name='phone',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
