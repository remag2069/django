# Generated by Django 2.2.3 on 2019-07-05 10:14

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(max_length=30)),
                ('student_id', models.IntegerField()),
                ('date_of_join', models.DateTimeField(default=datetime.datetime(2019, 7, 5, 10, 14, 39, 109050, tzinfo=utc))),
            ],
        ),
    ]
