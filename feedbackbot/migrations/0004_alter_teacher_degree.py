# Generated by Django 5.0.1 on 2024-02-06 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedbackbot', '0003_alter_classschedule_day_alter_classschedule_end_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='degree',
            field=models.CharField(choices=[('master', 'Magistr'), ('bachelor', 'Bakalavr'), ('academic', 'Akademik'), ('drscience', 'Doktorant'), ('phd', 'Professor')], max_length=10),
        ),
    ]