# Generated by Django 4.1 on 2022-08-20 22:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_remove_post_featured'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo_subtext', models.CharField(max_length=250)),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
    ]
