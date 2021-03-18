# Generated by Django 3.1 on 2021-03-16 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentapp', '0003_auto_20210315_2131'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='email',
            field=models.EmailField(default=1, max_length=254, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='teacher',
            name='password',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='student',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]