# Generated by Django 3.2.4 on 2021-06-15 11:34

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pica', '0005_departemen_departemen2user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='topik',
            name='solution',
        ),
        migrations.AddField(
            model_name='topik',
            name='action',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Solution'),
        ),
        migrations.AlterField(
            model_name='topik',
            name='problem',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Problem'),
        ),
    ]
