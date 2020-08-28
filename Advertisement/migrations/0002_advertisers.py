# Generated by Django 3.0.8 on 2020-07-27 16:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Advertisement', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Advertisers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('page_name', models.CharField(blank=True, max_length=255)),
                ('page_likes', models.BigIntegerField(default=0, null=True)),
                ('followers', models.BigIntegerField(default=0, null=True)),
                ('page_created_date', models.DateTimeField(blank=True)),
                ('company_type', models.CharField(blank=True, max_length=255)),
                ('people_manage_page', models.BigIntegerField(default=0, null=True)),
                ('countries_manage_page', models.BigIntegerField(default=0, null=True)),
                ('active_add', models.BigIntegerField(default=0, null=True)),
                ('inactive_add', models.BigIntegerField(default=0, null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category', to='Advertisement.Category')),
            ],
        ),
    ]
