# Generated by Django 2.2.4 on 2019-10-23 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_blog_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='photo',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]