# Generated by Django 3.2.12 on 2022-02-20 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_app', '0002_alter_book_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='qty',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='book',
            name='desc',
            field=models.TextField(default=''),
        ),
    ]
