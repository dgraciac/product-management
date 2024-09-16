# Generated by Django 5.1.1 on 2024-09-16 08:45

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('photo_url', models.CharField(max_length=1024, null=True)),
                ('creator', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='creator', to=settings.AUTH_USER_MODEL)),
                ('last_modifier', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='last_modifier', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
