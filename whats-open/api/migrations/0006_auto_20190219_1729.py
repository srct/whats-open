# Generated by Django 2.0.10 on 2019-02-19 22:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20190129_1215'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alert',
            name='url',
            field=models.URLField(blank=True, verbose_name='Reference URL'),
        ),
    ]