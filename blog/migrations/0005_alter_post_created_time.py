# Generated by Django 4.0.3 on 2022-04-16 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_postcomment_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
