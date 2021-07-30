# Generated by Django 3.2.4 on 2021-06-15 13:03

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pica', '0006_auto_20210615_1834'),
    ]

    operations = [
        migrations.AlterField(
            model_name='departemen',
            name='departemen2user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user2departemen', to=settings.AUTH_USER_MODEL, verbose_name='Direktur in charge: '),
        ),
        migrations.AlterField(
            model_name='topik',
            name='action',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Action'),
        ),
    ]
