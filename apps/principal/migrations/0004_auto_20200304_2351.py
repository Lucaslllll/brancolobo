# Generated by Django 2.2.4 on 2020-03-05 02:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0003_auto_20200304_2345'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='details',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='ingredients',
            field=models.ManyToManyField(blank=True, to='principal.Ingredients'),
        ),
    ]
