# Generated by Django 3.2.8 on 2022-05-11 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentname',
            name='image',
            field=models.ImageField(default='', upload_to='images/'),
            preserve_default=False,
        ),
    ]
