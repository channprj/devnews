# Generated by Django 2.2.2 on 2019-07-16 21:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('links', '0003_auto_20190717_0628'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-updated_at', '-created_at'], 'verbose_name': '댓글'},
        ),
        migrations.AlterModelOptions(
            name='link',
            options={'ordering': ['-updated_at', '-created_at'], 'verbose_name': '링크'},
        ),
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action', models.PositiveSmallIntegerField(default=1)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('link', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='links.Link')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '투표',
                'ordering': ['-created_at'],
            },
        ),
    ]