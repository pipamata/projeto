# Generated by Django 3.2.4 on 2021-07-05 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0005_alter_propostas_cronologia'),
    ]

    operations = [
        migrations.AlterField(
            model_name='propostas',
            name='cronologia',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
