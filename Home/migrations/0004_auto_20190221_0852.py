# Generated by Django 2.1.4 on 2019-02-21 02:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0003_snippet_home_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Home',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=100)),
                ('type', models.CharField(default='', max_length=100)),
                ('price', models.IntegerField(default='')),
                ('photo', models.ImageField(blank=True, upload_to='home_image')),
                ('description', models.TextField(default='', max_length=1000)),
                ('location', models.CharField(default='', max_length=100)),
                ('contacts', models.CharField(default='', max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='Snippet',
        ),
    ]
