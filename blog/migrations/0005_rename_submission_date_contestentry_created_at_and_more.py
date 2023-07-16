# Generated by Django 4.2.1 on 2023-07-16 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_contestentry'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contestentry',
            old_name='submission_date',
            new_name='created_at',
        ),
        migrations.RemoveField(
            model_name='contestentry',
            name='name',
        ),
        migrations.AddField(
            model_name='contestentry',
            name='first_name',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='contestentry',
            name='last_name',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='contestentry',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='contestentry',
            name='image',
            field=models.ImageField(upload_to='uploads/'),
        ),
    ]
