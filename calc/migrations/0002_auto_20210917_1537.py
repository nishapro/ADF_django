# Generated by Django 3.2.7 on 2021-09-17 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calc', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requesttable',
            name='pincode',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='requesttable',
            name='salary',
            field=models.IntegerField(),
        ),
    ]
