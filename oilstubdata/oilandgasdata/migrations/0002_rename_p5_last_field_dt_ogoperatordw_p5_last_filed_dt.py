# Generated by Django 4.1.5 on 2023-02-10 08:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oilandgasdata', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ogoperatordw',
            old_name='p5_last_field_dt',
            new_name='p5_last_filed_dt',
        ),
    ]
