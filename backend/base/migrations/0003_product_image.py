# Generated by Django 4.1.7 on 2023-02-26 01:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_order_shippingaddress_review_orderitem'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, default='/placeholder.png', null=True, upload_to=''),
        ),
    ]
