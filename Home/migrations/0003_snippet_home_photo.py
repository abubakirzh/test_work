# Generated by Django 2.1.4 on 2019-02-20 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0002_snippet_home_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='snippet',
            name='home_photo',
            field=models.ImageField(blank=True, upload_to='home_image'),
        ),
    ]
