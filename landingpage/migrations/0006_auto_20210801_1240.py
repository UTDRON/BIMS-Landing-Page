# Generated by Django 3.1.4 on 2021-08-01 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landingpage', '0005_auto_20210801_1231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='name',
            field=models.CharField(help_text='Name', max_length=50),
        ),
    ]
