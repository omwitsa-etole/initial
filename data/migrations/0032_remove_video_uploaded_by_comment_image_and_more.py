# Generated by Django 4.0.3 on 2022-04-04 16:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0031_alter_comment_video'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='uploaded_by',
        ),
        migrations.AddField(
            model_name='comment',
            name='image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='data.image'),
        ),
        migrations.AlterField(
            model_name='image',
            name='title',
            field=models.CharField(max_length=50),
        ),
    ]
