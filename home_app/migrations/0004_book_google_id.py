# Generated by Django 3.2.12 on 2022-02-20 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_app', '0003_auto_20220220_1559'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='google_id',
            field=models.CharField(default=0, max_length=15),
        ),
    ]
