# Generated by Django 3.0.3 on 2020-03-09 02:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0011_auto_20200308_1756'),
    ]

    operations = [
        migrations.CreateModel(
            name='TecDashImages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500, null=True)),
                ('details', models.TextField()),
                ('image', models.ImageField(upload_to='image/how_use')),
            ],
        ),
    ]
