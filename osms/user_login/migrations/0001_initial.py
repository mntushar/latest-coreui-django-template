# Generated by Django 2.2.8 on 2020-09-19 00:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('gender', models.CharField(blank=True, choices=[('male', 'Male'), ('female', 'Female')], max_length=6, null=True)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('phone_number', models.IntegerField(blank=True, null=True)),
                ('email', models.EmailField(blank=True, max_length=100, null=True, unique=True)),
                ('occupation', models.CharField(blank=True, max_length=10, null=True)),
                ('home_address', models.TextField(blank=True, null=True)),
                ('password', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
    ]
