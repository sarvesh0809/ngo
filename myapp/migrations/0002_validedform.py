# Generated by Django 3.1.7 on 2021-04-27 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Validedform',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=254)),
                ('details', models.TextField()),
                ('bank_details', models.TextField()),
                ('amount', models.IntegerField()),
                ('pub_date', models.DateField()),
            ],
        ),
    ]