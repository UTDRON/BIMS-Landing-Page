# Generated by Django 3.1.4 on 2021-08-01 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landingpage', '0006_auto_20210801_1240'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]
