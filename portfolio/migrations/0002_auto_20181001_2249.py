# Generated by Django 2.1.1 on 2018-10-01 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolioitem',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
