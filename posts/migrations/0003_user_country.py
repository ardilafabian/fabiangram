# Generated by Django 3.2.7 on 2021-10-15 01:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_user_is_admin'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='country',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
