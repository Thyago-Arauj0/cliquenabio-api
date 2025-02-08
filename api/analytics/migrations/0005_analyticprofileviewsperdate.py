# Generated by Django 5.1.4 on 2025-02-07 18:23

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analytics', '0004_alter_analyticprofileviews_number_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AnalyticProfileViewsPerDate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.PositiveBigIntegerField(default=0, verbose_name='Número')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuário')),
            ],
        ),
    ]
