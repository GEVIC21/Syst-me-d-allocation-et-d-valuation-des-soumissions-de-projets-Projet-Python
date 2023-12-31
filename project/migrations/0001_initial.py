# Generated by Django 2.2.2 on 2019-10-22 16:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('total_marks', models.IntegerField()),
                ('description', models.TextField(blank=True, null=True)),
                ('files', models.FileField(blank=True, null=True, upload_to='project/')),
                ('slug', models.SlugField(unique=True)),
                ('teach_by', models.CharField(max_length=20)),
                ('start_date', models.DateTimeField(auto_now_add=True)),
                ('end_date', models.DateTimeField(blank=True, null=True)),
                ('semester', models.CharField(blank=True, max_length=20, null=True)),
                ('year', models.CharField(blank=True, max_length=10, null=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('publish_date', models.DateTimeField(blank=True, null=True)),
                ('course', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='courses.Courses')),
            ],
            options={
                'ordering': ['-publish_date', '-updated', '-timestamp'],
            },
        ),
        migrations.CreateModel(
            name='Submission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('submit_by', models.CharField(max_length=20)),
                ('file', models.FileField(upload_to='submission/')),
                ('marks', models.IntegerField()),
                ('assignment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.Assignment')),
            ],
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(default='unknown', max_length=120)),
                ('comment', models.CharField(max_length=2000)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('publish_date', models.DateTimeField(blank=True, null=True)),
                ('assignment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.Assignment')),
            ],
            options={
                'ordering': ['-publish_date', '-updated', '-timestamp'],
            },
        ),
    ]
