# Generated by Django 3.2.9 on 2021-11-20 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='作成日時')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='更新日時')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField(max_length=1000)),
                ('expired_at', models.DateField()),
            ],
            options={
                'abstract': False,
            },
        ),
    ]