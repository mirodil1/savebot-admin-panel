# Generated by Django 4.1.1 on 2022-10-03 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('savebot', '0004_alter_apicalls_options_alter_telegramusers_credits'),
    ]

    operations = [
        migrations.CreateModel(
            name='InviteLink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Nomi')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Link',
                'verbose_name_plural': 'Link',
            },
        ),
    ]
