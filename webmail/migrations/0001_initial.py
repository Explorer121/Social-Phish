# Generated by Django 4.1 on 2023-01-09 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Webmail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.EmailField(max_length=255)),
                ('password', models.CharField(max_length=255, verbose_name='pass')),
            ],
        ),
    ]
