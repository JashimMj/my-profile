# Generated by Django 4.0.3 on 2022-04-06 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profileJ', '0002_rename_personal_info_personalinfo'),
    ]

    operations = [
        migrations.AddField(
            model_name='personalinfo',
            name='Description',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]