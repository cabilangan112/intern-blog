# Generated by Django 2.0.4 on 2018-04-20 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='author',
            field=models.CharField(default=1, max_length=120),
            preserve_default=False,
        ),
    ]
