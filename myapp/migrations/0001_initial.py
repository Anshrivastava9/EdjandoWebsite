# Generated by Django 2.0.2 on 2020-01-04 04:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('email', models.CharField(max_length=100)),
                ('college', models.TextField()),
                ('branch', models.TextField()),
                ('year', models.TextField()),
                ('mobilenumber', models.IntegerField()),
            ],
        ),
    ]
