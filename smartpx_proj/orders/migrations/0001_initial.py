# Generated by Django 4.0.6 on 2022-07-14 14:47

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
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('email', models.CharField(max_length=500)),
                ('address', models.CharField(max_length=500)),
                ('city', models.CharField(max_length=500)),
                ('state', models.CharField(max_length=100)),
                ('transaction_id', models.CharField(default=0, max_length=150)),
                ('total_amount', models.CharField(default=0, max_length=150)),
                ('byer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]