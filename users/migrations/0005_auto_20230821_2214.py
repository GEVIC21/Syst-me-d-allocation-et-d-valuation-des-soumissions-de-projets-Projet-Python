# Generated by Django 2.2 on 2023-08-21 22:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20191118_0709'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='join_year',
            field=models.CharField(default='2023', max_length=10),
        ),
    ]
