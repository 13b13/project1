# Generated by Django 3.2.20 on 2023-08-14 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donate', '0003_auto_20230814_1248'),
    ]

    operations = [
        migrations.AddField(
            model_name='donate',
            name='id',
            field=models.BigAutoField(auto_created=True, default=2, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='donate',
            name='name',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
