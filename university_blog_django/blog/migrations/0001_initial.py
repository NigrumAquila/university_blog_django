# Generated by Django 2.2 on 2020-04-20 15:09

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('abbreviation', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'faculties',
            },
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Mark',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('value', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('hour', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=10)),
                ('surname', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50)),
                ('patronymic', models.CharField(max_length=50)),
                ('gender', models.CharField(choices=[('man', 'м'), ('woman', 'ж')], default='м', max_length=40)),
                ('birthday', models.DateTimeField(default=django.utils.timezone.now)),
                ('group', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='blog.Group')),
            ],
        ),
        migrations.CreateModel(
            name='Lecturer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('surname', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50)),
                ('patronymic', models.CharField(max_length=50)),
                ('faculty', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='blog.Faculty')),
                ('post', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='blog.Post')),
            ],
        ),
        migrations.CreateModel(
            name='GroupSubject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exam_test', models.CharField(choices=[('exam', 'экзамен'), ('offset', 'зачет')], default='зачет', max_length=40)),
                ('group', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='blog.Group')),
                ('lecturer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='blog.Lecturer')),
                ('subject', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='blog.Subject')),
            ],
            options={
                'db_table': 'blog_group_subject',
            },
        ),
        migrations.CreateModel(
            name='ExamMark',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('group_subject', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='blog.GroupSubject')),
                ('mark', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='blog.Mark')),
                ('student', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='blog.Student')),
            ],
            options={
                'db_table': 'blog_exam_mark',
            },
        ),
    ]