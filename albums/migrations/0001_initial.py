# Generated by Django 3.0.3 on 2021-03-24 02:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('artist', models.CharField(max_length=250)),
                ('label', models.CharField(max_length=100)),
                ('sku', models.CharField(max_length=20)),
            ],
        ),
    ]
