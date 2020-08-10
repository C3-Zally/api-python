# Generated by Django 3.0.8 on 2020-08-10 05:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('states', '0001_initial'),
        ('cities', '0001_initial'),
        ('countries', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Date time on which object was created.', verbose_name='created at')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='Date time on which object was last updated.', verbose_name='updated at')),
                ('report_id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateField(blank=True)),
                ('infections', models.BigIntegerField()),
                ('active_cases', models.BigIntegerField()),
                ('new_cases', models.BigIntegerField()),
                ('new_deaths', models.BigIntegerField()),
                ('deaths', models.BigIntegerField()),
                ('samples_proccesed', models.BigIntegerField()),
                ('recovered', models.BigIntegerField()),
                ('city_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cities.City')),
                ('country_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='countries.Country')),
                ('state_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='states.State')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
