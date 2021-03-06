# Generated by Django 3.0.7 on 2020-10-02 06:04

from django.db import migrations, models
import gdstorage.storage


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='file',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('map_name', models.CharField(max_length=200)),
                ('map_data', models.FileField(storage=gdstorage.storage.GoogleDriveStorage(), upload_to='maps')),
            ],
        ),
        migrations.CreateModel(
            name='teachercourse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_id', models.ManyToManyField(to='main.courses')),
                ('teacher_id', models.ManyToManyField(to='main.teacher')),
            ],
        ),
        migrations.CreateModel(
            name='studentcourse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_id', models.ManyToManyField(to='main.courses')),
                ('student_id', models.ManyToManyField(to='main.student')),
            ],
        ),
    ]
