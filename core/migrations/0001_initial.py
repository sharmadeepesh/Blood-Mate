# Generated by Django 3.0 on 2020-03-09 12:13

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
            name='group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=3)),
                ('gives', models.CharField(max_length=3)),
                ('receives', models.CharField(max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='Donor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.IntegerField()),
                ('phone_number', models.IntegerField()),
                ('occupation', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=20)),
                ('state', models.CharField(max_length=20)),
                ('blood_group', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='core.group')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
