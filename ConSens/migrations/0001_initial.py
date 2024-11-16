# Generated by Django 5.1.3 on 2024-11-16 14:55

import django.contrib.auth.models
import django.contrib.auth.validators
import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Modulo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('ultima_modificacion', models.DateTimeField(auto_now=True)),
                ('nombre', models.CharField(max_length=64, unique=True)),
                ('grupo', models.CharField(max_length=32, unique=True)),
                ('ubicacion', models.CharField(max_length=64)),
                ('tipo', models.CharField(choices=[('Wifi', 'Wifi industrial'), ('LoRa', 'Long Range')], max_length=16)),
            ],
            options={
                'verbose_name': 'Modulo',
                'verbose_name_plural': 'Modulos',
            },
        ),
        migrations.CreateModel(
            name='Registros',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('fecha', models.DateField(auto_now_add=True)),
                ('hora', models.TimeField(auto_now_add=True)),
                ('ubicacion', models.CharField(max_length=64)),
                ('temperatura', models.IntegerField()),
                ('humedad', models.DecimalField(decimal_places=2, max_digits=5)),
                ('presion', models.IntegerField()),
                ('modulo', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='ConSens.modulo')),
            ],
            options={
                'verbose_name': 'Registro',
                'verbose_name_plural': 'Registros',
            },
        ),
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('es_administrador', models.BooleanField(default=False)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'Usuario',
                'verbose_name_plural': 'Usuarios',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='ValorCriticoTemperatura',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('fecha', models.DateField(auto_now_add=True)),
                ('hora', models.TimeField(auto_now_add=True)),
                ('temperatura_maxima', models.IntegerField()),
                ('temperatura_minima', models.IntegerField()),
                ('modulo', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='ConSens.modulo')),
                ('usuario', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Valor critico de temperatura',
                'verbose_name_plural': 'Valores criticos de temperatura',
            },
        ),
        migrations.CreateModel(
            name='ValorCriticoPresion',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('fecha', models.DateField(auto_now_add=True)),
                ('hora', models.TimeField(auto_now_add=True)),
                ('presion_maxima', models.IntegerField()),
                ('presion_minima', models.IntegerField()),
                ('modulo', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='ConSens.modulo')),
                ('usuario', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Valor critico de presion',
                'verbose_name_plural': 'Valores criticos de presion',
            },
        ),
        migrations.CreateModel(
            name='ValorCriticoHumedad',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('fecha', models.DateField(auto_now_add=True)),
                ('hora', models.TimeField(auto_now_add=True)),
                ('humedad_maxima', models.DecimalField(decimal_places=2, max_digits=5)),
                ('humedad_minima', models.DecimalField(decimal_places=2, max_digits=5)),
                ('modulo', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='ConSens.modulo')),
                ('usuario', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Valor critico de humedad',
                'verbose_name_plural': 'Valores criticos de humedad',
            },
        ),
    ]
