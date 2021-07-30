# Generated by Django 3.2.4 on 2021-06-20 13:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pica', '0017_auto_20210620_0913'),
    ]

    operations = [
        migrations.AlterField(
            model_name='peserta',
            name='bod',
            field=models.BooleanField(default=False, verbose_name='Apakah masuk dalam list BOD?'),
        ),
        migrations.AlterField(
            model_name='peserta',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True, verbose_name='Email address'),
        ),
        migrations.AlterField(
            model_name='peserta',
            name='name',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Nama Peserta'),
        ),
        migrations.AlterField(
            model_name='peserta',
            name='peserta2company',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='company2peserta', to='pica.company', verbose_name='Company'),
        ),
        migrations.AlterField(
            model_name='peserta',
            name='peserta2departemen',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='pica.departemen', verbose_name='Departemen'),
        ),
    ]
