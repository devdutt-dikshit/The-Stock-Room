# Generated by Django 3.0 on 2020-04-27 22:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_productcat_productsitems'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productsitems',
            name='desc',
            field=models.TextField(),
        ),
    ]
