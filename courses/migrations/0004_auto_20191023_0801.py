# Generated by Django 2.2.2 on 2019-10-23 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_auto_20191023_0548'),
    ]

    operations = [
        migrations.AddField(
            model_name='takes',
            name='section',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3')], default='1', max_length=5),
        ),
        migrations.AddField(
            model_name='teaches',
            name='section',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3')], default='1', max_length=5),
        ),
    ]
