# Generated by Django 3.0.8 on 2020-08-12 02:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Care',
            fields=[
                ('care_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=50)),
                ('slug', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=4000)),
            ],
        ),
    ]
