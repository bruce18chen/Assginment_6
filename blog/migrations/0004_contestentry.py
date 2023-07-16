# Generated by Django 4.2.1 on 2023-07-16 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_topic_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContestEntry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('image', models.ImageField(upload_to='contest_entries/')),
                ('submission_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]