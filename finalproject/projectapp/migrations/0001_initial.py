# Generated by Django 2.2 on 2019-06-07 18:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Pharmacist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pharmname', models.CharField(max_length=255)),
                ('pharmage', models.IntegerField()),
                ('pharmwage', models.IntegerField()),
                ('user', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'Pharmacist',
            },
        ),
        migrations.CreateModel(
            name='Technician',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('techname', models.CharField(max_length=255)),
                ('techage', models.IntegerField()),
                ('techwage', models.IntegerField()),
                ('user', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'Technician',
            },
        ),
        migrations.CreateModel(
            name='Shift',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shiftname', models.CharField(max_length=255)),
                ('pharmname', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='projectapp.Pharmacist')),
                ('techname', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='projectapp.Technician')),
                ('user', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Medication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('medname', models.CharField(max_length=255)),
                ('meddescription', models.TextField(blank=True, null=True)),
                ('medusage', models.TextField(blank=True, null=True)),
                ('medwarning', models.CharField(max_length=255)),
                ('medquantity', models.IntegerField()),
                ('medcost', models.IntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'Medication',
            },
        ),
    ]