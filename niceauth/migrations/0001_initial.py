# Generated by Django 4.2.13 on 2024-06-12 07:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NiceAuthRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, null=True, verbose_name='Updated At')),
                ('request_no', models.CharField(max_length=30, unique=True)),
                ('enc_data', models.TextField()),
                ('integrity_value', models.TextField()),
                ('token_version_id', models.CharField(max_length=100)),
                ('key', models.CharField(max_length=32)),
                ('iv', models.CharField(max_length=32)),
            ],
            options={
                'verbose_name': 'Nice Auth Request',
                'verbose_name_plural': 'Nice Auth Requests',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='NiceAuthResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, null=True, verbose_name='Updated At')),
                ('result_data', models.JSONField()),
                ('request', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='niceauth.niceauthrequest')),
            ],
            options={
                'verbose_name': 'Nice Auth Result',
                'verbose_name_plural': 'Nice Auth Results',
                'ordering': ['-created_at'],
            },
        ),
    ]
