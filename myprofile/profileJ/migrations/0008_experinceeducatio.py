# Generated by Django 4.0.3 on 2022-04-07 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profileJ', '0007_rename_working_exper_working_experience'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExperinceEducatio',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('year', models.CharField(blank=True, max_length=255, null=True)),
                ('EXPERIENCE', models.CharField(blank=True, max_length=255, null=True)),
                ('EDUCATION', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
    ]
