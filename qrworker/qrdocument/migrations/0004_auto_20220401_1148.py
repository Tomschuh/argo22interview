# Generated by Django 3.2.12 on 2022-04-01 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qrdocument', '0003_alter_qrdocument_expiration_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='qrdocument',
            name='image',
        ),
        migrations.AddField(
            model_name='qrdocument',
            name='imageBase64',
            field=models.TextField(default=''),
        ),
    ]