# Generated by Django 4.0.3 on 2022-04-02 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0007_image_video_category_alter_user_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='description',
            field=models.TextField(blank=True, help_text='Video Description', null=True),
        ),
    ]
