# Generated by Django 3.2.4 on 2021-06-20 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pica', '0018_auto_20210620_2019'),
    ]

    operations = [
        migrations.AddField(
            model_name='forum',
            name='group_code',
            field=models.CharField(blank=True, max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='forum',
            name='keterangan',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
