# Generated by Django 3.2 on 2023-03-15 18:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_reviewrating'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reviewrating',
            name='ip',
        ),
    ]