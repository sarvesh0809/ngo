# Generated by Django 3.1.7 on 2021-04-29 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_contact'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ngoform',
            name='mfile',
        ),
        migrations.AddField(
            model_name='ngoform',
            name='m1file',
            field=models.FileField(default='', upload_to=''),
        ),
        migrations.AddField(
            model_name='ngoform',
            name='m2file',
            field=models.FileField(default='', upload_to=''),
        ),
        migrations.AddField(
            model_name='ngoform',
            name='m3file',
            field=models.FileField(default='', upload_to=''),
        ),
    ]
