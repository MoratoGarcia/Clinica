# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-26 13:32
from __future__ import unicode_literals

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
            name='Chequeo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField(auto_now=True)),
                ('graduacion', models.CharField(max_length=100)),
                ('observaciones', models.TextField()),
                ('compra', models.BooleanField(default=True)),
                ('armazon', models.CharField(choices=[(b'opcion1', b'Opcion1'), (b'opcion2', b'Opcion2')], default=b'opcion1', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='OptExp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enfermedad', models.CharField(max_length=200)),
                ('dato2', models.CharField(blank=True, max_length=100, null=True)),
                ('dato3', models.CharField(blank=True, max_length=100, null=True)),
                ('paciente', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.CharField(choices=[(b'opcion1', b'Opcion1'), (b'opcion2', b'Opcion2')], default=b'opcion2', max_length=20)),
                ('nombre', models.CharField(max_length=100)),
                ('edad', models.IntegerField()),
                ('sexo', models.CharField(max_length=10)),
                ('direccion', models.TextField()),
                ('fecha_nacimiento', models.DateField(blank=True, null=True)),
                ('foto', models.ImageField(blank=True, upload_to=b'users/%Y/%m/%d')),
            ],
        ),
        migrations.AddField(
            model_name='chequeo',
            name='expediente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='chequeos', to='optica.OptExp'),
        ),
    ]
