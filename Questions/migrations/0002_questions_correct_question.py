# Generated by Django 3.0.5 on 2021-05-30 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Questions', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='questions',
            name='correct_question',
            field=models.CharField(blank=True, max_length=2, null=True),
        ),
    ]