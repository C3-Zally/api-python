# Generated by Django 3.0.8 on 2020-08-10 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Date time on which object was created.', verbose_name='created at')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='Date time on which object was last updated.', verbose_name='updated at')),
                ('country_id', models.AutoField(primary_key=True, serialize=False)),
                ('country_name', models.CharField(blank=True, max_length=50)),
                ('alpha2code', models.CharField(max_length=5)),
                ('alpha3code', models.CharField(max_length=5)),
                ('capital', models.CharField(max_length=50)),
                ('region', models.CharField(max_length=50)),
                ('subregion', models.CharField(max_length=50)),
                ('flag', models.CharField(max_length=500)),
                ('population', models.BigIntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
