# Generated by Django 3.2.4 on 2021-07-07 12:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pica', '0037_rename_status_activity_status_act'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='activity',
            name='status_act',
        ),
    ]
