# Generated by Django 3.1.1 on 2020-09-28 16:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agendas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='horario',
            name='horario',
            field=models.TimeField(choices=[(datetime.time(8, 0), '08:00'), (datetime.time(8, 30), '08:30'), (datetime.time(9, 0), '09:00'), (datetime.time(9, 30), '09:30'), (datetime.time(10, 0), '10:00'), (datetime.time(10, 30), '10:30'), (datetime.time(11, 0), '11:00'), (datetime.time(11, 30), '11:30'), (datetime.time(12, 0), '12:00'), (datetime.time(
                12, 30), '12:30'), (datetime.time(13, 0), '13:00'), (datetime.time(13, 30), '13:30'), (datetime.time(14, 0), '14:00'), (datetime.time(14, 30), '14:30'), (datetime.time(15, 0), '15:00'), (datetime.time(15, 30), '15:30'), (datetime.time(16, 0), '16:00'), (datetime.time(16, 30), '16:30'), (datetime.time(17, 0), '17:00')], unique=True),
        ),
    ]
