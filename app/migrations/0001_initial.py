# Generated by Django 4.2.5 on 2023-09-28 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Stu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('dob', models.DateField()),
            ],
            options={
                'db_table': 'Stu',
            },
        ),
    ]
