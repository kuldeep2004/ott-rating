# Generated by Django 4.0.6 on 2023-03-02 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ottratings', '0002_remove_web_landscape_remove_web_portrait'),
    ]

    operations = [
        migrations.AddField(
            model_name='web',
            name='landscape',
            field=models.CharField(default='https://wallpapercave.com/wp/wp7955488.jpg', max_length=200),
        ),
        migrations.AddField(
            model_name='web',
            name='portrait',
            field=models.CharField(default='https://i.pinimg.com/564x/e3/82/55/e38255b8fad2209e3f0252e8b4ba0612.jpg', max_length=200),
        ),
    ]