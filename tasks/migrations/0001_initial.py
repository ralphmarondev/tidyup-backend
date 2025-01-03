# Generated by Django 5.1.4 on 2025-01-03 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('priority', models.PositiveSmallIntegerField(choices=[(1, 'HIGH'), (2, 'MEDIUM'), (3, 'LOW')])),
                ('status', models.PositiveSmallIntegerField(choices=[(1, 'IN-PROGRESS'), (2, 'COMPLETED')])),
                ('is_deleted', models.BooleanField(default=False)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]