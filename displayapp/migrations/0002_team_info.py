# Generated by Django 3.2.16 on 2022-10-19 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('displayapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='team_info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='pics')),
                ('about', models.TextField()),
            ],
        ),
    ]
