# Generated by Django 5.0.2 on 2024-03-19 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SupportBot', '0002_alter_supportusers_username'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdminsID',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('admin_id', models.BigIntegerField()),
                ('group_id', models.BigIntegerField()),
            ],
            options={
                'verbose_name_plural': 'Adminlar',
                'db_table': 'admins',
            },
        ),
    ]
