# Generated by Django 4.0.3 on 2022-04-07 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profileJ', '0005_personalinfo_address_personalinfo_age_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='working_Exper',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('YEARS_OF_EXPERIENCE', models.CharField(blank=True, max_length=255, null=True)),
                ('COMPLETEDPROJECTS', models.CharField(blank=True, max_length=255, null=True)),
                ('HAPPYCUSTOMERS', models.CharField(blank=True, max_length=255, null=True)),
                ('AWARDSWON', models.CharField(blank=True, max_length=255, null=True)),
                ('HTML', models.CharField(blank=True, max_length=255, null=True)),
                ('CSS', models.CharField(blank=True, max_length=255, null=True)),
                ('JAVASCRIPT', models.CharField(blank=True, max_length=255, null=True)),
                ('PYTHON', models.CharField(blank=True, max_length=255, null=True)),
                ('JQUERY', models.CharField(blank=True, max_length=255, null=True)),
                ('PYTHON_DJANGO', models.CharField(blank=True, max_length=255, null=True)),
                ('ORACLE', models.CharField(blank=True, max_length=255, null=True)),
                ('DATABASE', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
    ]
