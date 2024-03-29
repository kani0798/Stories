# Generated by Django 3.1 on 2020-09-17 07:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Story',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='photos')),
                ('name', models.CharField(max_length=30)),
                ('lastUpdated', models.DateTimeField(auto_now=True)),
                ('seen', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('photo', 'Photo'), ('video', 'Video')], max_length=5)),
                ('length', models.PositiveIntegerField(default=3)),
                ('src', models.FileField(upload_to='files')),
                ('lastUpdated', models.DateTimeField(auto_now=True)),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('seen', models.BooleanField(default=False)),
                ('story', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stories', to='main.story')),
            ],
        ),
    ]
