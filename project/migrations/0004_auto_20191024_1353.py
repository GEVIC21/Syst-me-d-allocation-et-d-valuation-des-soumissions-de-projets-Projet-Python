# Generated by Django 2.2.2 on 2019-10-24 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0003_assignment_types'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignment',
            name='description',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]
