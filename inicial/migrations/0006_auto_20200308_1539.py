# Generated by Django 2.2.4 on 2020-03-08 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inicial', '0005_auto_20200308_1537'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photoprodutoafterbefore',
            name='photo',
            field=models.ImageField(null=True, upload_to='case'),
        ),
    ]