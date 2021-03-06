# Generated by Django 3.1.4 on 2021-08-01 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landingpage', '0004_auto_20210801_1230'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='address',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='contact',
            name='contact_no',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='contact',
            name='industry_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='contact',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='contact',
            name='otp',
            field=models.CharField(default='', max_length=10),
        ),
    ]
