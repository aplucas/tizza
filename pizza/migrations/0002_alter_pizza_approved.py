# Generated by Django 3.2.4 on 2021-06-13 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizza', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pizza',
            name='approved',
            field=models.BooleanField(default=False),
        ),
    ]
