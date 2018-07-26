# Generated by Django 2.0.5 on 2018-07-26 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_fixture_migration'),
    ]

    operations = [
        migrations.AddField(
            model_name='batch',
            name='running_months',
            field=models.ManyToManyField(blank=True, related_name='batches', to='main.Month'),
        ),
        migrations.AlterField(
            model_name='student',
            name='phone',
            field=models.CharField(blank=True, max_length=13, null=True),
        ),
    ]
