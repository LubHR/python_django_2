# Generated by Django 5.1.1 on 2024-09-26 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CarModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=50)),
                ('price', models.IntegerField()),
                ('year', models.IntegerField()),
            ],
            options={
                'db_table': 'cars',
            },
        ),
    ]
