# Generated by Django 3.2.5 on 2021-10-27 02:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DATABASE', '0002_alter_blogmaindatabase_hashnumber'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogmaindatabase',
            name='dateCreated',
        ),
        migrations.AddField(
            model_name='blogmaindatabase',
            name='dateTimeCreated',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]