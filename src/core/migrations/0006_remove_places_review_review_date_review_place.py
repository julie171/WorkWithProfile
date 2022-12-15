# Generated by Django 4.1.2 on 2022-12-15 16:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_remove_places_other_info_review_places_review'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='places',
            name='review',
        ),
        migrations.AddField(
            model_name='review',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='review',
            name='place',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='core.places'),
        ),
    ]
