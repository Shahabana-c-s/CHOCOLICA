# Generated by Django 4.1.3 on 2023-01-02 15:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CHOCOLICA_APP', '0004_productdb_category_alter_productdb_price'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productdb',
            old_name='category',
            new_name='Category',
        ),
    ]