# Generated by Django 5.1.3 on 2024-11-27 19:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('YouOweMe', '0003_deadbeat_debt'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deadbeat',
            name='debt',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='debt', to='YouOweMe.debt'),
        ),
    ]
