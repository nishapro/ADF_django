# Generated by Django 3.2.7 on 2021-09-17 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='requestTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('mid_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('dob', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=50)),
                ('nationality', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('current_city', models.CharField(max_length=50)),
                ('pincode', models.IntegerField(max_length=50)),
                ('qualification', models.CharField(max_length=50)),
                ('salary', models.IntegerField(max_length=50)),
                ('pan', models.CharField(max_length=50)),
                ('request_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='responseTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('request_id', models.IntegerField()),
                ('response', models.CharField(max_length=50)),
                ('reason', models.CharField(max_length=300)),
            ],
        ),
    ]
