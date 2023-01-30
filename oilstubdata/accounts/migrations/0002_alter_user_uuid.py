# Generated by Django 4.1.5 on 2023-01-24 09:16

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='uuid',
            field=models.UUIDField(db_index=True, default=uuid.uuid4, primary_key=True, serialize=False, unique=True),
        ),
    ]
