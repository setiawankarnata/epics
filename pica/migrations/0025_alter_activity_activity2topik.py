# Generated by Django 3.2.4 on 2021-06-22 03:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pica', '0024_alter_topik_due_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='activity2topik',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='topik2activity', to='pica.topik'),
        ),
    ]