# Generated by Django 3.1.2 on 2020-11-30 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tacoapp', '0004_food_weekday'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='migas',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='food',
            name='vegan',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='food',
            name='bean',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='food',
            name='potato',
            field=models.IntegerField(default=0),
        ),
    ]