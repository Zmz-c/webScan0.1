# Generated by Django 3.2.7 on 2021-09-26 04:17

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='urlManager',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(help_text='text', max_length=256)),
                ('urlTime', models.DateTimeField(verbose_name=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(blank=True, max_length=32, verbose_name='用户名')),
                ('password', models.CharField(help_text='text', max_length=64)),
                ('email', models.EmailField(max_length=60)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
            ],
        ),
        migrations.CreateModel(
            name='uV',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('open_url', models.CharField(help_text='text', max_length=256)),
                ('open_port', models.CharField(help_text='text', max_length=256)),
                ('open_sql', models.CharField(help_text='text', max_length=256)),
                ('url', models.CharField(help_text='text', max_length=256)),
                ('publish', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webScan.urlmanager')),
            ],
        ),
    ]
