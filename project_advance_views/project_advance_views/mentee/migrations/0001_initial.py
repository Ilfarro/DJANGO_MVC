# Generated by Django 2.1.5 on 2019-02-13 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mentee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('quote', models.TextField(max_length=255)),
                ('picture', models.CharField(max_length=255)),
            ],
        ),
    ]
