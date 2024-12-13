# Generated by Django 4.2.11 on 2024-11-07 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_cart_service'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='category',
            field=models.CharField(default=33, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cart',
            name='price',
            field=models.DecimalField(decimal_places=2, default=11, max_digits=5),
            preserve_default=False,
        ),
    ]
