# Generated by Django 2.2.2 on 2019-10-22 16:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_id', models.CharField(max_length=20, unique=True)),
                ('title', models.CharField(max_length=120)),
                ('department', models.CharField(choices=[('CSE', 'CSE'), ('EE', 'EE'), ('ME', 'ME'), ('ECE', 'ECE'), ('Civil', 'Civil')], default='unknown', max_length=120)),
                ('credits', models.IntegerField()),
                ('slug', models.SlugField(unique=True)),
                ('content', models.TextField(blank=True, null=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('publish_date', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'ordering': ['-publish_date', '-updated', '-timestamp'],
            },
        ),
        migrations.CreateModel(
            name='Teaches',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teacher_id', models.CharField(max_length=20)),
                ('semester', models.CharField(choices=[('spring', 'spring'), ('fall', 'fall'), ('summer', 'summer')], default='unknown', max_length=20)),
                ('year', models.CharField(max_length=10)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('publish_date', models.DateTimeField(blank=True, null=True)),
                ('course_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='courses.Courses')),
            ],
            options={
                'ordering': ['-publish_date', '-updated', '-timestamp'],
            },
        ),
        migrations.CreateModel(
            name='Takes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_id', models.CharField(max_length=20)),
                ('semester', models.CharField(choices=[('spring', 'spring'), ('fall', 'fall'), ('summer', 'summer')], default='unknown', max_length=20)),
                ('year', models.CharField(max_length=10)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('publish_date', models.DateTimeField(blank=True, null=True)),
                ('course_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='courses.Courses')),
            ],
            options={
                'ordering': ['-publish_date', '-updated', '-timestamp'],
            },
        ),
    ]
