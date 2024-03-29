# Generated by Django 3.0.5 on 2021-06-01 08:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import djongo.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Exams',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('slug', models.CharField(max_length=255)),
                ('innitiated_date', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('subject', models.CharField(max_length=50)),
                ('level_of_different', models.FloatField(default=2.5)),
                ('medium_score', models.FloatField(default=0)),
                ('time', models.IntegerField()),
                ('list_id_questions', models.TextField(null=True)),
                ('list_id_questions_group', models.TextField(blank=True, null=True)),
                ('amount_questions', models.IntegerField(default=0)),
                ('amount_view_user', models.IntegerField(default=0)),
                ('amount_do', models.IntegerField(default=0)),
                ('comments', djongo.models.fields.JSONField(blank=True, default=dict, null=True)),
                ('options', djongo.models.fields.JSONField(blank=True, default=dict, null=True)),
                ('id_author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
