# Generated by Django 3.2.4 on 2021-06-28 07:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20210628_0448'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.DO_NOTHING, to='products.category'),
            preserve_default=False,
        ),
    ]