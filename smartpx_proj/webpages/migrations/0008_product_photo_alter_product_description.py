# Generated by Django 4.0.5 on 2022-07-09 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webpages', '0007_rename_is_featured_product_best_seller_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='photo',
            field=models.ImageField(default=0, upload_to='media/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(),
        ),
    ]
