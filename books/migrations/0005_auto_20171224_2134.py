# Generated by Django 2.0 on 2017-12-24 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_auto_20171224_2106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='headshot',
            field=models.ImageField(upload_to='author_headshots'),
        ),
    ]