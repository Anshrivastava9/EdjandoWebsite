# Generated by Django 2.0.2 on 2020-01-04 14:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_auto_20200104_1927'),
    ]

    operations = [
        migrations.RenameField(
            model_name='company',
            old_name='comapanyname',
            new_name='companyname',
        ),
    ]
