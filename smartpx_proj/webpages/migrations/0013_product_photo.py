# Generated by Django 4.0.6 on 2022-07-14 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webpages', '0012_alter_product_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='photo',
            field=models.ImageField(blank=True, upload_to='media'),
        ),
    ]