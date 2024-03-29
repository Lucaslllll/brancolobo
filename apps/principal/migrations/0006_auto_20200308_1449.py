# Generated by Django 2.2.4 on 2020-03-08 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0005_auto_20200306_1548'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cases',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(max_length=255, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='How_Use',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('details', models.TextField()),
                ('image', models.ImageField(upload_to='image/how_use')),
            ],
        ),
        migrations.CreateModel(
            name='Initial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('subtitle', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Video_Description',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('details', models.TextField()),
                ('video', models.FileField(upload_to='video')),
            ],
        ),
        migrations.AlterField(
            model_name='product',
            name='ingredients',
            field=models.ManyToManyField(blank=True, to='principal.Ingredients'),
        ),
    ]
