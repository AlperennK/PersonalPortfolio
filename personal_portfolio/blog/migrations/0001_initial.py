# Generated by Django 3.0.7 on 2020-07-01 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=200)),
                ('description', models.TextField(max_length=10000)),
                ('date', models.DateField()),
                ('image', models.ImageField(upload_to='blog/images/')),
                ('url', models.URLField(blank=True)),
            ],
        ),
    ]
