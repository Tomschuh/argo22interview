# Generated by Django 3.2.12 on 2022-04-01 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qrdocument', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='qrdocument',
            old_name='iamge',
            new_name='image',
        ),
        migrations.AlterField(
            model_name='qrdocument',
            name='expiration_date',
            field=models.DateField(blank=True),
        ),
    ]