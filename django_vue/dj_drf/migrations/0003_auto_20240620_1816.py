# Generated by Django 3.2.23 on 2024-06-20 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dj_drf', '0002_auto_20240620_1706'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('age', models.IntegerField()),
                ('sex', models.BooleanField(default=1)),
                ('class_null', models.CharField(max_length=255)),
            ],
        ),
        migrations.DeleteModel(
            name='RegisterUser',
        ),
    ]
