# Generated by Django 5.0.2 on 2024-10-04 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedbackbot', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classschedule',
            name='start_time',
            field=models.CharField(choices=[('08:30:00', '1-PARA, 08:30'), ('10:00:00', '2-PARA, 10:00'), ('11:30:00', '3-PARA, 11:30'), ('13:30:00', '4-PARA, 13:30'), ('15:00:00', '5-PARA, 15:00'), ('16:30:00', '6-PARA, 16:30')], max_length=15),
        ),
    ]