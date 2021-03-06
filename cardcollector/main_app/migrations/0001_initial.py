# Generated by Django 3.1.6 on 2021-02-08 01:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('attributes', models.CharField(max_length=50)),
                ('types', models.CharField(max_length=50)),
                ('description', models.TextField(max_length=200)),
                ('atk', models.IntegerField()),
                ('defense', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Deck',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField(max_length=200)),
                ('cards', models.ManyToManyField(blank=True, to='main_app.Card')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('grade', models.CharField(choices=[('S', 'S-Class'), ('A', 'A-Class'), ('B', 'B-Class'), ('C', 'C-Class'), ('D', 'D-Class')], default='S', max_length=1)),
                ('deck', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.deck')),
            ],
        ),
    ]
