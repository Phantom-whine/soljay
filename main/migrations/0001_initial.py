# Generated by Django 5.1.2 on 2024-10-22 12:30

import django.db.models.deletion
import django.utils.timezone
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=250)),
                ('image', models.ImageField(upload_to='images/')),
                ('description', models.TextField()),
                ('job_type', models.CharField(max_length=250)),
                ('children_info', models.CharField(max_length=250)),
                ('country', models.CharField(max_length=20)),
                ('city', models.CharField(max_length=100)),
                ('job_start', models.CharField(max_length=40)),
                ('time_of_stay', models.CharField(max_length=40)),
                ('letter_to_applicant', models.TextField()),
                ('has_pet', models.CharField(choices=[('yes', 'yes'), ('no', 'no')], max_length=3)),
                ('age_group', models.CharField(default=None, max_length=50)),
                ('working_hours', models.CharField(max_length=50)),
                ('salary', models.PositiveIntegerField(default=0)),
                ('gender_required', models.CharField(choices=[('male', 'Male'), ('female', 'Female')], max_length=10)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Applied',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payed', models.BooleanField(default=False)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('job', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='main.job')),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
    ]
