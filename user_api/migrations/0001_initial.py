# Generated by Django 3.1.4 on 2020-12-03 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('mobile_number', models.CharField(max_length=10)),
                ('password', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=50)),
                ('dob', models.DateField()),
            ],
        ),
    ]
