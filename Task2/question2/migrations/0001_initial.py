# Generated by Django 5.1.3 on 2024-11-15 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField(max_length=400)),
                ('start_date', models.DateTimeField(auto_now_add=True)),
                ('end_date', models.DateField()),
            ],
        ),
    ]