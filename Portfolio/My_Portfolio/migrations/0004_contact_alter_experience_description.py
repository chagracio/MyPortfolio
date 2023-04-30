# Generated by Django 4.1.7 on 2023-04-27 23:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('My_Portfolio', '0003_personalinfo_contact_personalinfo_facebook_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField()),
                ('subject', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='experience',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]