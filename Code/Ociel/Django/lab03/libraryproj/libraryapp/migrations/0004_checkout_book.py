# Generated by Django 2.0.3 on 2018-03-26 19:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('libraryapp', '0003_checkout'),
    ]

    operations = [
        migrations.AddField(
            model_name='checkout',
            name='book',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='libraryapp.Book'),
        ),
    ]
