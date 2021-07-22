# Generated by Django 3.2.5 on 2021-07-21 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='merchantuser',
            name='is_added_by_admin',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='merchantuser',
            name='profile_pic',
            field=models.FileField(default='', upload_to=''),
        ),
    ]