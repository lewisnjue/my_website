# Generated by Django 5.0.3 on 2024-03-07 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_profile_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, upload_to='posts_images'),
        ),
    ]