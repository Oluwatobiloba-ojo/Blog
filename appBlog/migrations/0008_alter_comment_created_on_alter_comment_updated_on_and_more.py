# Generated by Django 5.0.4 on 2024-04-24 03:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appBlog', '0007_alter_post_createdat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_on',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='updated_on',
            field=models.DateField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='createdAt',
            field=models.DateField(auto_now_add=True),
        ),
    ]
