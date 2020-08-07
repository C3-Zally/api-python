# Generated by Django 3.0.8 on 2020-08-07 00:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cities', '0001_initial'),
        ('states', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='city',
            name='state_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='states.State'),
        ),
    ]
