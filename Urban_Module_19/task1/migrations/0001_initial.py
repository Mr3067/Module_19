# Generated by Django 5.1.1 on 2024-09-13 10:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Buyer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('balance', models.DecimalField(decimal_places=2, max_digits=5)),
                ('age', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('cost', models.DecimalField(decimal_places=2, max_digits=5)),
                ('size', models.DecimalField(decimal_places=2, max_digits=5)),
                ('description', models.TextField()),
                ('age_limited', models.BooleanField(default=False)),
                ('DecimalField', models.DecimalField(decimal_places=2, max_digits=5)),
                ('BooleanField', models.BooleanField()),
                ('buyer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='game', to='task1.buyer')),
            ],
        ),
    ]
