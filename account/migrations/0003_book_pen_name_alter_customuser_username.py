# Generated by Django 4.0.3 on 2023-02-23 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_remove_book_pen_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='pen_name',
            field=models.CharField(default='None', max_length=100),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='username',
            field=models.CharField(default='User', max_length=30),
        ),
    ]
