# Generated by Django 5.0.3 on 2024-03-28 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Compromissos',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('event_date', models.DateTimeField()),
                ('creation_date', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
