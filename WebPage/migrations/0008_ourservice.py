# Generated by Django 3.2.7 on 2021-09-09 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebPage', '0007_staff_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='OurService',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ServiceName', models.CharField(max_length=100, null=True)),
                ('Image', models.ImageField(upload_to='')),
            ],
        ),
    ]
