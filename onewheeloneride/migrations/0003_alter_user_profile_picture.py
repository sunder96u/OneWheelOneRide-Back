# Generated by Django 4.0 on 2023-07-26 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onewheeloneride', '0002_alter_user_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile_picture',
            field=models.CharField(default='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS1VAWlUdnhzQgtyss_G-WaeDPGgj3XBQx95A&usqp=CAU', max_length=250),
        ),
    ]
