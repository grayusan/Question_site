# Generated by Django 3.0.8 on 2020-08-10 09:26

from django.db import migrations
import markdownx.models


class Migration(migrations.Migration):

    dependencies = [
        ('situmon', '0006_auto_20200808_0437'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='text',
            field=markdownx.models.MarkdownxField(help_text='Markdown形式で書いてください。', verbose_name='コメント本文'),
        ),
        migrations.AlterField(
            model_name='reply',
            name='text',
            field=markdownx.models.MarkdownxField(help_text='Markdown形式で書いてください。', verbose_name='返信本文'),
        ),
    ]
