# Generated by Django 3.2.4 on 2021-06-15 07:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pica', '0004_auto_20210615_1338'),
    ]

    operations = [
        migrations.AddField(
            model_name='departemen',
            name='departemen2user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user2departemen', to=settings.AUTH_USER_MODEL, verbose_name='Direktur in charge: '),
        ),
    ]