# Generated by Django 2.2.2 on 2019-07-16 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('links', '0005_auto_20190717_0654'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vote',
            name='action',
            field=models.NullBooleanField(choices=[(None, ''), (True, 'Upvote'), (False, 'Downvote')], default=None, max_length=3),
        ),
    ]
