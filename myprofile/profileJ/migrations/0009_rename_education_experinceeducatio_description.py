# Generated by Django 4.0.3 on 2022-04-07 07:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profileJ', '0008_experinceeducatio'),
    ]

    operations = [
        migrations.RenameField(
            model_name='experinceeducatio',
            old_name='EDUCATION',
            new_name='Description',
        ),
    ]
