# Generated by Django 4.1.1 on 2022-09-28 13:02

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ApiCalls',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('status', models.BooleanField()),
                ('created_at', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Channels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=255)),
                ('language', multiselectfield.db.fields.MultiSelectField(choices=[('uz', 'Uzbek'), ('ru', 'Russian'), ('en', 'English'), ('uk', 'Ukrain'), ('ar', 'Arabic')], max_length=10, verbose_name='TIL')),
                ('created_at', models.DateTimeField(verbose_name="QO'SHILGAN VAQTI")),
            ],
            options={
                'verbose_name': 'Kanallar',
                'verbose_name_plural': 'Kanallar',
            },
        ),
        migrations.CreateModel(
            name='TelegramUsers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=255, verbose_name="TO'LIQ ISM")),
                ('username', models.CharField(blank=True, max_length=255, null=True)),
                ('joined_date', models.DateField(verbose_name="QO'SHILGAN VAQTI")),
            ],
            options={
                'verbose_name': 'Telegram obunachilar',
                'verbose_name_plural': 'Telegram obunachilar',
            },
        ),
    ]
