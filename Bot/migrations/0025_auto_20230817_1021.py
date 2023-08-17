# Generated by Django 3.2.19 on 2023-08-17 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Bot', '0024_bot_order_choice_alter_bot_comment_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='bot',
            name='latitude',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='bot',
            name='longitude',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='bot',
            name='adress',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
