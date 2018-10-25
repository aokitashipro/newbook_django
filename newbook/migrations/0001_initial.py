# Generated by Django 2.1.2 on 2018-10-25 01:27

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DayCharge',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('plan_id', models.CharField(max_length=10)),
                ('date', models.DateField(blank=True, null=True)),
                ('rank', models.CharField(max_length=3)),
                ('person_num', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(6)])),
                ('charge', models.IntegerField(default=0)),
            ],
            options={
                'db_table': 'dayCharge',
            },
        ),
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('hotel_id', models.CharField(max_length=10, primary_key=True, serialize=False, unique=True)),
                ('hotel_name_ja', models.CharField(max_length=255)),
                ('hotel_name_en', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'hotel',
            },
        ),
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('plan_id', models.CharField(max_length=10)),
                ('plan_name', models.CharField(max_length=10)),
                ('hotel_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='newbook.Hotel')),
            ],
            options={
                'db_table': 'plan',
            },
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('room_id', models.CharField(max_length=10)),
                ('room_name', models.CharField(max_length=10)),
                ('hotel_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='newbook.Hotel')),
            ],
            options={
                'db_table': 'room',
            },
        ),
        migrations.CreateModel(
            name='RoomStock',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('room_id', models.CharField(max_length=10)),
                ('date', models.DateField(blank=True, null=True)),
                ('qty', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(1000)])),
                ('reserved_out', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(1000)])),
                ('hotel_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='newbook.Hotel')),
            ],
            options={
                'db_table': 'roomStock',
            },
        ),
        migrations.AddField(
            model_name='daycharge',
            name='hotel_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='newbook.Hotel'),
        ),
        migrations.AlterUniqueTogether(
            name='room',
            unique_together={('hotel_id', 'room_id')},
        ),
        migrations.AlterUniqueTogether(
            name='plan',
            unique_together={('hotel_id', 'plan_id')},
        ),
    ]
