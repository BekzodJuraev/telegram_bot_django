# Generated by Django 4.1.2 on 2023-07-22 17:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Bot', '0012_rename_bot_bot_diary'),
    ]

    operations = [
        migrations.AddField(
            model_name='diary',
            name='add_item',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Bot.add_item'),
        ),
    ]
