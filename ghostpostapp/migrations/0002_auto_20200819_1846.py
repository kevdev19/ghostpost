# Generated by Django 3.1 on 2020-08-19 18:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ghostpostapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='roastboastmodel',
            old_name='roast_boast',
            new_name='is_boast',
        ),
    ]
