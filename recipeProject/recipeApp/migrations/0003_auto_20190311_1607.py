# Generated by Django 2.2 on 2019-03-11 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipeApp', '0002_auto_20190311_1604'),
    ]

    operations = [
        migrations.AddField(
            model_name='newprofilemodel',
            name='password1',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='newprofilemodel',
            name='password2',
            field=models.CharField(default='', max_length=200),
        ),
    ]
