# Generated by Django 3.2.4 on 2021-06-16 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pica', '0013_auto_20210616_1915'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topik',
            name='issued_date',
            field=models.DateField(auto_now=True, verbose_name='Issued Date'),
        ),
    ]
