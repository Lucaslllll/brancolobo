# Generated by Django 2.2.4 on 2020-03-08 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0006_auto_20200308_1449'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cases',
            name='image',
            field=models.ImageField(upload_to='image/cases'),
        ),
    ]
