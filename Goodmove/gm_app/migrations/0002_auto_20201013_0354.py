# Generated by Django 2.2 on 2020-10-13 03:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gm_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('genre', models.CharField(max_length=255)),
                ('length', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='movies',
            field=models.ManyToManyField(related_name='users', to='gm_app.Movie'),
        ),
    ]