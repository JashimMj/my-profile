# Generated by Django 4.0.3 on 2022-04-07 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profileJ', '0011_educatio'),
    ]

    operations = [
        migrations.CreateModel(
            name='project',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Image', models.ImageField(blank=True, null=True, upload_to='projects')),
                ('Link', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
    ]
