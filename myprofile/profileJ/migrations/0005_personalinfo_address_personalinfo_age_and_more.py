# Generated by Django 4.0.3 on 2022-04-07 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profileJ', '0004_personalinfo_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='personalinfo',
            name='Address',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='personalinfo',
            name='Age',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='personalinfo',
            name='Email',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='personalinfo',
            name='First_Name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='personalinfo',
            name='Freelance',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='personalinfo',
            name='Langages',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='personalinfo',
            name='Last_Name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='personalinfo',
            name='Nationality',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='personalinfo',
            name='Phone',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
