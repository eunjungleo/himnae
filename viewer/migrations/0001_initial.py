# Generated by Django 3.0.8 on 2020-08-06 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('url', models.URLField()),
                ('date', models.DateTimeField(auto_now=True)),
                ('korean', models.TextField(null=True)),
                ('chinese', models.TextField(null=True)),
                ('turkmen', models.TextField(null=True)),
            ],
        ),
    ]