# Generated by Django 3.1.7 on 2021-03-05 01:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0002_offer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='stock',
        ),
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.CharField(default='Available', max_length=650),
            preserve_default=False,
        ),
    ]
