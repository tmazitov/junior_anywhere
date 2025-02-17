# Generated by Django 5.1.2 on 2024-11-11 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0004_company_llc_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='llc_number',
        ),
        migrations.AddField(
            model_name='company',
            name='LLC_Number',
            field=models.CharField(default='', max_length=55, unique=True),
        ),
    ]
