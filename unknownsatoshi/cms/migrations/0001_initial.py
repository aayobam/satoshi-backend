# Generated by Django 3.2.9 on 2021-12-02 20:51

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField()),
                ('post', ckeditor_uploader.fields.RichTextUploadingField()),
                ('featured_stories', models.BooleanField(default=False)),
                ('latest_news', models.BooleanField(default=False)),
                ('latest_articles', models.BooleanField(default=False)),
                ('featured_image', models.ImageField(blank=True, default='default.png', null=True, upload_to='blog_images/')),
                ('premium', models.BooleanField(default=False)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Cms',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('title', models.CharField(max_length=200)),
                ('entry', models.TextField(blank=True, null=True)),
                ('stoploss', models.TextField(blank=True, null=True)),
                ('tp_target', models.IntegerField(blank=True, default=0, null=True)),
                ('tp_achieved', models.IntegerField(blank=True, default=0, null=True)),
                ('profit', models.IntegerField(blank=True, default=0, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ('created',),
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('courses', models.TextField(blank=True, null=True)),
                ('course_link', models.TextField(blank=True, null=True)),
                ('featured_image', models.ImageField(blank=True, default='default.png', null=True, upload_to='course_images/')),
            ],
        ),
        migrations.CreateModel(
            name='Newsletter',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('email', models.EmailField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('slug', models.SlugField(unique=True)),
                ('desc', models.TextField()),
                ('price', models.IntegerField(default=0)),
                ('discount_price', models.IntegerField(default=0)),
                ('discount', models.IntegerField(default=0)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ('created_on',),
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('product_name', models.TextField(blank=True, null=True)),
                ('product_link', models.TextField(blank=True, null=True)),
                ('price', models.TextField(blank=True, null=True)),
                ('featured_image', models.ImageField(blank=True, default='default.png', null=True, upload_to='product_images/')),
            ],
        ),
        migrations.CreateModel(
            name='SubscriptionHistory',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('email', models.EmailField(max_length=200, unique=True)),
                ('full_name', models.CharField(max_length=200)),
                ('phone_no', models.CharField(max_length=11, unique=True)),
                ('amount_paid', models.SmallIntegerField(default=0)),
                ('reference', models.CharField(max_length=200, unique=True)),
                ('transaction_id', models.CharField(max_length=200)),
                ('status', models.CharField(max_length=200)),
                ('start_date', models.DateTimeField(auto_now_add=True)),
                ('expiry_date', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=False)),
                ('plan', models.ForeignKey(default='monthly plan', on_delete=django.db.models.deletion.CASCADE, to='cms.plan')),
            ],
        ),
    ]
