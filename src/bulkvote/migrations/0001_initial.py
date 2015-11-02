# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('choice', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('item', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='UserChoice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('choice', models.ForeignKey(related_name='userchoices', to='bulkvote.Choice')),
                ('item', models.ForeignKey(related_name='userchoices', to='bulkvote.Item')),
            ],
        ),
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('uuid', models.UUIDField(default=uuid.uuid4, unique=True, editable=False)),
                ('description', models.TextField()),
                ('author', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='item',
            name='vote',
            field=models.ForeignKey(related_name='items', to='bulkvote.Vote'),
        ),
        migrations.AddField(
            model_name='choice',
            name='vote',
            field=models.ForeignKey(related_name='choices', to='bulkvote.Vote'),
        ),
    ]
