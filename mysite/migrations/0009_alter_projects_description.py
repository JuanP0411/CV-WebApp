# Generated by Django 4.2.7 on 2024-02-13 00:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0008_remove_certificate_is_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='description',
            field=models.CharField(max_length=1000),
        ),
    ]
