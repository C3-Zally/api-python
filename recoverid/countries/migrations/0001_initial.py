# Generated by Django 3.0.8 on 2020-08-09 01:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Date time on wich object was created.', verbose_name='created at')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='Date time on wich object was last updated.', verbose_name='updated at')),
                ('deleted_at', models.DateTimeField(auto_now_add=True, help_text='Date time on wich object was deleted.', verbose_name='deleted at')),
                ('status', models.CharField(choices=[('ACTIVE', 'ACTIVE'), ('INACTIVE', 'INACTIVE')], max_length=8)),
                ('flag', models.CharField(max_length=500)),
                ('country_id', models.AutoField(primary_key=True, serialize=False)),
                ('country_name', models.CharField(max_length=50)),
                ('alpha2code', models.CharField(max_length=5)),
                ('alpha3code', models.CharField(max_length=5)),
                ('capital', models.CharField(max_length=50)),
                ('region', models.CharField(max_length=50)),
                ('subregion', models.CharField(max_length=50)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
