# Generated by Django 2.0.3 on 2018-03-15 16:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lab02_todo', '0002_auto_20180313_1704'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Todo',
            new_name='TodoItem',
        ),
        migrations.RenameField(
            model_name='todoitem',
            old_name='item',
            new_name='text',
        ),
    ]
