# Generated by Django 3.2.4 on 2021-06-16 01:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pica', '0009_alter_topik_topik2user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='departemen',
            name='departemen2user',
        ),
        migrations.AddField(
            model_name='departemen',
            name='dept_head_in_charge',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='departemen',
            name='dir_in_charge',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='departemen',
            name='email_dept_head_in_charge',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='departemen',
            name='email_dir_in_charge',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]
