# Generated by Django 2.1.7 on 2019-03-21 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commentinfo',
            name='comment_num',
            field=models.IntegerField(default=0),
        ),
    ]
