# Generated by Django 4.1 on 2022-09-04 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fullstackapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactdetails',
            name='email',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='contactdetails',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='contactdetails',
            name='number',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='contactdetails',
            name='subject',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='contactdetails',
            name='text',
            field=models.TextField(null=True),
        ),
    ]
