# Generated by Django 2.2.4 on 2020-03-08 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0009_auto_20200308_1617'),
    ]

    operations = [
        migrations.AddField(
            model_name='how_use',
            name='title',
            field=models.CharField(max_length=500, null=True),
        ),
    ]
