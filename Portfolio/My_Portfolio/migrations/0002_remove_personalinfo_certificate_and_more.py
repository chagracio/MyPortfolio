# Generated by Django 4.1.7 on 2023-04-27 01:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('My_Portfolio', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='personalinfo',
            name='certificate',
        ),
        migrations.RemoveField(
            model_name='personalinfo',
            name='education',
        ),
        migrations.RemoveField(
            model_name='personalinfo',
            name='experience',
        ),
        migrations.RemoveField(
            model_name='personalinfo',
            name='language',
        ),
        migrations.RemoveField(
            model_name='personalinfo',
            name='project',
        ),
        migrations.RemoveField(
            model_name='personalinfo',
            name='soft_skill',
        ),
        migrations.RemoveField(
            model_name='personalinfo',
            name='tech_skill',
        ),
        migrations.AddField(
            model_name='personalinfo',
            name='certificate',
            field=models.ManyToManyField(to='My_Portfolio.certificates'),
        ),
        migrations.AddField(
            model_name='personalinfo',
            name='education',
            field=models.ManyToManyField(to='My_Portfolio.education'),
        ),
        migrations.AddField(
            model_name='personalinfo',
            name='experience',
            field=models.ManyToManyField(to='My_Portfolio.experience'),
        ),
        migrations.AddField(
            model_name='personalinfo',
            name='language',
            field=models.ManyToManyField(to='My_Portfolio.languages'),
        ),
        migrations.AddField(
            model_name='personalinfo',
            name='project',
            field=models.ManyToManyField(to='My_Portfolio.projects'),
        ),
        migrations.AddField(
            model_name='personalinfo',
            name='soft_skill',
            field=models.ManyToManyField(to='My_Portfolio.soft_skills'),
        ),
        migrations.AddField(
            model_name='personalinfo',
            name='tech_skill',
            field=models.ManyToManyField(to='My_Portfolio.technical_skills'),
        ),
    ]
