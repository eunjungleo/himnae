# Generated by Django 3.1 on 2020-08-10 03:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('viewer', '0002_content_eng'),
    ]

    operations = [
        migrations.AddField(
            model_name='content',
            name='q1',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='content',
            name='q2',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='content',
            name='q3',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='content',
            name='q4',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='content',
            name='q5',
            field=models.IntegerField(null=True),
        ),
    ]
