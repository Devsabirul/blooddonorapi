# Generated by Django 4.1.3 on 2022-11-05 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='is_available',
            field=models.BooleanField(default=False, null=True, verbose_name='Is available'),
        ),
    ]
