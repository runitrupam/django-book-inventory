# Generated by Django 3.2.12 on 2022-02-20 21:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_app', '0005_alter_book_desc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='google_id',
            field=models.CharField(default=0, max_length=15, unique=True),
        ),
    ]
