# Generated by Django 3.0.1 on 2020-08-06 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipes',
            old_name='body',
            new_name='description',
        ),
        migrations.RemoveField(
            model_name='recipes',
            name='post_date',
        ),
        migrations.AddField(
            model_name='author',
            name='bio',
            field=models.TextField(default='asdf', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='recipes',
            name='instructions',
            field=models.TextField(default='asdf'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='recipes',
            name='time_required',
            field=models.CharField(default='asdf', max_length=50),
            preserve_default=False,
        ),
    ]
