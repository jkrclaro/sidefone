# Generated by Django 3.0.1 on 2020-02-15 23:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Podcast',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('author', models.CharField(max_length=255)),
                ('img', models.URLField()),
                ('feed', models.URLField()),
                ('website', models.URLField(blank=True, null=True)),
                ('itunes_id', models.CharField(max_length=255)),
                ('summary', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'podcasts',
            },
        ),
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subscriptions', to='accounts.Account')),
                ('podcast', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subscribers', to='podcasts.Podcast')),
            ],
            options={
                'db_table': 'subscriptions',
            },
        ),
        migrations.CreateModel(
            name='Episode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('published_at', models.DateTimeField()),
                ('duration', models.CharField(max_length=255)),
                ('url', models.URLField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('podcast', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='episodes', to='podcasts.Podcast')),
            ],
            options={
                'db_table': 'episodes',
                'unique_together': {('name', 'published_at', 'duration', 'url', 'podcast')},
            },
        ),
    ]
