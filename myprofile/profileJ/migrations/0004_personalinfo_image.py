# Generated by Django 4.0.3 on 2022-04-06 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profileJ', '0003_personalinfo_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='personalinfo',
            name='Image',
            field=models.ImageField(blank=True, null=True, upload_to='User_image'),
        ),
    ]
