# Generated by Django 3.2.5 on 2021-08-28 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_auto_20210721_1041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adminuser',
            name='profile_pic',
            field=models.FileField(default='', upload_to=''),
        ),
        migrations.AlterField(
            model_name='customeruser',
            name='profile_pic',
            field=models.FileField(default='', upload_to=''),
        ),
        migrations.AlterField(
            model_name='staffuser',
            name='profile_pic',
            field=models.FileField(default='', upload_to=''),
        ),
    ]
