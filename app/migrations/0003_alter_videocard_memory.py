# Generated by Django 5.0.3 on 2024-03-15 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_videocard_memory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='videocard',
            name='memory',
            field=models.IntegerField(),
        ),
    ]
