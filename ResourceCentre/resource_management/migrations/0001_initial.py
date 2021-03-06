# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2017-11-04 12:56
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('library_resources', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BookIssueTracker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='book_issued', to='library_resources.Book')),
                ('member_involved', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='member_book', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='MemberBooksTaken',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('books', models.ManyToManyField(related_name='books_issued', to='library_resources.Book')),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='current_member', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
