# Generated by Django 4.2.7 on 2024-01-13 03:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0005_userprofile_age_userprofile_email_userprofile_github_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='experience',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to='experiences'),
        ),
    ]
