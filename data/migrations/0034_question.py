# Generated by Django 4.0.3 on 2022-04-06 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0033_remove_comment_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(blank=True, max_length=300, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('more_description', models.TextField(blank=True, null=True)),
            ],
            options={
                'ordering': ['-date_created'],
            },
        ),
    ]