# Generated by Django 4.1.2 on 2023-07-22 21:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Bot', '0018_alter_bot_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='diary',
            name='diary',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='related_diaries', to='Bot.bot'),
        ),
    ]
