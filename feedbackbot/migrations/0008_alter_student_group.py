# Generated by Django 5.0.1 on 2024-02-10 17:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedbackbot', '0007_alter_student_course_num'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='feedbackbot.group'),
        ),
    ]