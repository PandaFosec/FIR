# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2017-01-27 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fir_notifications', '0002_user_preference'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='notificationpreference',
            options={'ordering': ['user', 'event', 'method'], 'verbose_name': 'notification preference', 'verbose_name_plural': 'notification preferences'},
        ),
        migrations.AlterField(
            model_name='methodconfiguration',
            name='key',
            field=models.CharField(choices=[(b'email', b'Email'), (b'xmpp', b'XMPP')], max_length=60, verbose_name='method'),
        ),
    ]
