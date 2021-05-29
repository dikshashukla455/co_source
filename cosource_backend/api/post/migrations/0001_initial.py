# Generated by Django 3.2.3 on 2021-05-29 17:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
                ('description', models.CharField(max_length=200)),
                ('phone', models.CharField(blank=True, default=None, max_length=20, null=True)),
                ('link', models.CharField(blank=True, default=None, max_length=20, null=True)),
                ('country', models.CharField(default='India', max_length=30)),
                ('region', models.CharField(default='South', max_length=30)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('assigned', models.BooleanField(default=False)),
                ('validated', models.BooleanField(default=False)),
                ('accepted', models.BooleanField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PostStatusModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('detail', models.TextField(null=True)),
                ('video', models.FileField(null=True, upload_to='videos/')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='post.post')),
            ],
        ),
    ]
