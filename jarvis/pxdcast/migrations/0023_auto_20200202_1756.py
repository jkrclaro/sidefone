# Generated by Django 3.0.1 on 2020-02-02 17:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pxdcast', '0022_auto_20200202_1446'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='episode',
            unique_together=set(),
        ),
    ]