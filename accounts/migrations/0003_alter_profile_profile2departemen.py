# Generated by Django 3.2.4 on 2021-06-15 04:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pica', '0003_auto_20210615_1146'),
        ('accounts', '0002_profile_profile2departemen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile2departemen',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='pica.departemen', verbose_name='Departemen'),
        ),
    ]
