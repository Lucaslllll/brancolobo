# Generated by Django 2.2.4 on 2020-03-05 02:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inicial', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Description',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('details', models.TextField()),
            ],
        ),
    ]