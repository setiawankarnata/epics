# Generated by Django 3.2.4 on 2021-06-27 10:09

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('pica', '0026_activity_due_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='topik',
            name='group_code',
            field=models.CharField(blank=True, max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='activity',
            name='date_activity',
            field=models.DateField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='Date Activity'),
        ),
    ]
