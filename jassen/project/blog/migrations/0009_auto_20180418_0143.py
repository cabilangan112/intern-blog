# Generated by Django 2.0.4 on 2018-04-18 01:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20180418_0134'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='category_title',
            new_name='title',
        ),
        migrations.RenameField(
            model_name='tags',
            old_name='tags_title',
            new_name='title',
        ),
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Category'),
        ),
        migrations.AlterField(
            model_name='post',
            name='tags',
            field=models.ManyToManyField(related_name='Post', to='blog.Tags'),
        ),
    ]