# Generated by Django 3.2.8 on 2021-11-02 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homePage', '0003_alter_register_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='gender',
            field=models.CharField(choices=[('Female', 'Female'), ('male', 'male'), ('none', 'none')], max_length=8),
        ),
    ]