# Generated by Django 4.1.7 on 2023-03-18 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0008_menu'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='url_name',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
