# Generated by Django 3.0.5 on 2024-01-02 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecom', '0012_orders_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='profile_pic',
            field=models.ImageField(default='Screenshot_3.png', upload_to='profile_pic/CustomerProfilePic/'),
        ),
    ]
