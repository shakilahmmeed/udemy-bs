# Generated by Django 3.0.7 on 2020-07-25 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0004_auto_20200725_1244'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='thumbnail',
            field=models.ImageField(default='media/none/nothumb.jpg', upload_to='courses'),
        ),
    ]