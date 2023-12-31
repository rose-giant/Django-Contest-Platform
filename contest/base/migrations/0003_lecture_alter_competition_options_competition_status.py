# Generated by Django 4.2.2 on 2023-06-13 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_topic_competition_host_alter_competition_id_award_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lecture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('link', models.CharField(max_length=200)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AlterModelOptions(
            name='competition',
            options={'ordering': ['-updated', '-created']},
        ),
        migrations.AddField(
            model_name='competition',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]
