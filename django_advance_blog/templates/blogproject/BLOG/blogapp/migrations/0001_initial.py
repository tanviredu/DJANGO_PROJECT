# Generated by Django 2.0 on 2019-05-02 08:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Catagory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('slug', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('slug', models.SlugField(max_length=150)),
                ('author', models.CharField(max_length=150)),
                ('description', models.TextField()),
                ('created_at', models.DateField()),
                ('image', models.ImageField(blank=True, upload_to='product/%Y/%m/%d')),
                ('catagory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blogapp.Catagory')),
            ],
        ),
    ]
