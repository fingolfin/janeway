# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-08-03 09:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.manager
import submission.models


class Migration(migrations.Migration):

    dependencies = [
        ('submission', '0055_auto_20210629_0641'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='article',
            managers=[
                ('allarticles', django.db.models.manager.Manager()),
                ('objects', submission.models.ArticleManager()),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='abstract_cy',
            field=models.TextField(blank=True, help_text='Please avoid pasting content from word processors as they can add unwanted styling to the abstract. You can retype the abstract here or copy and paste it into notepad/a plain text editor before pasting here.', null=True),
        ),
        migrations.AddField(
            model_name='article',
            name='abstract_de',
            field=models.TextField(blank=True, help_text='Please avoid pasting content from word processors as they can add unwanted styling to the abstract. You can retype the abstract here or copy and paste it into notepad/a plain text editor before pasting here.', null=True),
        ),
        migrations.AddField(
            model_name='article',
            name='abstract_en',
            field=models.TextField(blank=True, help_text='Please avoid pasting content from word processors as they can add unwanted styling to the abstract. You can retype the abstract here or copy and paste it into notepad/a plain text editor before pasting here.', null=True),
        ),
        migrations.AddField(
            model_name='article',
            name='abstract_fr',
            field=models.TextField(blank=True, help_text='Please avoid pasting content from word processors as they can add unwanted styling to the abstract. You can retype the abstract here or copy and paste it into notepad/a plain text editor before pasting here.', null=True),
        ),
        migrations.AddField(
            model_name='article',
            name='abstract_nl',
            field=models.TextField(blank=True, help_text='Please avoid pasting content from word processors as they can add unwanted styling to the abstract. You can retype the abstract here or copy and paste it into notepad/a plain text editor before pasting here.', null=True),
        ),
        migrations.AddField(
            model_name='article',
            name='title_cy',
            field=models.CharField(help_text='Your article title', max_length=999, null=True),
        ),
        migrations.AddField(
            model_name='article',
            name='title_de',
            field=models.CharField(help_text='Your article title', max_length=999, null=True),
        ),
        migrations.AddField(
            model_name='article',
            name='title_en',
            field=models.CharField(help_text='Your article title', max_length=999, null=True),
        ),
        migrations.AddField(
            model_name='article',
            name='title_fr',
            field=models.CharField(help_text='Your article title', max_length=999, null=True),
        ),
        migrations.AddField(
            model_name='article',
            name='title_nl',
            field=models.CharField(help_text='Your article title', max_length=999, null=True),
        ),
    ]