# Generated by Django 5.0.4 on 2024-04-22 01:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appBlog', '0006_comment_updated_on_alter_comment_author_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='createdAt',
            field=models.DateField(),
        ),
    ]
