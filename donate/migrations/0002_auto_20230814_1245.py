# Generated by Django 3.2.20 on 2023-08-14 03:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donate', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='donate',
            name='kind',
        ),
        migrations.RemoveField(
            model_name='donate',
            name='last_update',
        ),
        migrations.AlterField(
            model_name='donate',
            name='condition',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='donate',
            name='upgrade',
            field=models.CharField(blank=True, max_length=2, null=True),
        ),
    ]
