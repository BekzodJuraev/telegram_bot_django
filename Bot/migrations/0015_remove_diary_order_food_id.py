# Generated by Django 4.1.2 on 2023-07-22 20:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Bot', '0014_remove_diary_order_food_diary_order_food_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='diary',
            name='order_food_id',
        ),
    ]
