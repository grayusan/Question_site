# Generated by Django 3.0.8 on 2020-08-07 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('situmon', '0004_auto_20200808_0250'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='text',
            field=models.TextField(null=True, verbose_name='本文'),
        ),
        migrations.AlterField(
            model_name='reply',
            name='text',
            field=models.TextField(null=True, verbose_name='本文'),
        ),
    ]