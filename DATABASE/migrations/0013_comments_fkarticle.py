# Generated by Django 3.2.5 on 2021-12-04 04:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('DATABASE', '0012_auto_20211204_0354'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='fkArticle',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='DATABASE.blogmaindatabase'),
        ),
    ]