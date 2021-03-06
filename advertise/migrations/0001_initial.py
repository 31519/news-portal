# Generated by Django 3.1.5 on 2021-05-19 09:49

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
            name='Categories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categories_adv', models.CharField(max_length=100, unique=True)),
                ('slug', models.SlugField(max_length=100)),
                ('created_date', models.DateField(auto_now_add=True)),
                ('updated_date', models.DateField(auto_now=True)),
            ],
            options={
                'verbose_name': 'adv_category',
                'verbose_name_plural': 'adv_categories',
            },
        ),
        migrations.CreateModel(
            name='Advertise',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adv_heading', models.CharField(blank=True, max_length=100)),
                ('adv_descriptions', models.TextField(blank=True, max_length=500)),
                ('adv_images', models.ImageField(default='images/adv/no_img.jpg/', upload_to='images/adv/')),
                ('adv_conclude', models.CharField(blank=True, max_length=100)),
                ('adv_created_date', models.DateField(auto_now_add=True)),
                ('adv_updated_date', models.DateField(auto_now=True)),
                ('adv_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='advertise.categories')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
