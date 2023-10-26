# Generated by Django 4.2.6 on 2023-10-26 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LogData',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('store_id', models.IntegerField()),
                ('user_id', models.IntegerField()),
                ('content', models.CharField(max_length=255)),
            ],
        ),
    ]
