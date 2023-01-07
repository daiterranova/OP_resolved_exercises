# Generated by Django 4.1.5 on 2023-01-05 20:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('apellido', models.CharField(max_length=32)),
                ('birth_date', models.DateField()),
                ('death_date', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=200)),
                ('year', models.PositiveBigIntegerField()),
                ('duration', models.PositiveBigIntegerField()),
                ('director', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.director')),
            ],
        ),
    ]
