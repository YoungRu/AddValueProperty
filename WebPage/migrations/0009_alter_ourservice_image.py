# Generated by Django 3.2.7 on 2021-11-17 06:05

from django.db import migrations
import s3direct.fields


class Migration(migrations.Migration):

    dependencies = [
        ('WebPage', '0008_ourservice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ourservice',
            name='Image',
            field=s3direct.fields.S3DirectField(),
        ),
    ]