# Generated by Django 3.2.4 on 2021-06-15 06:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pica', '0003_auto_20210615_1146'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='topik',
            name='problem_owner',
        ),
        migrations.AlterField(
            model_name='topik',
            name='topik2affco',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='affco2topik', to='pica.affco', verbose_name='Problem Owner'),
        ),
    ]