# Generated by Django 3.2.20 on 2023-08-14 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donate', '0004_auto_20230814_1422'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donate',
            name='last_update',
            field=models.DateField(auto_now_add=True, default="2023-08-14"),
            preserve_default=False,
        ),
    ]
