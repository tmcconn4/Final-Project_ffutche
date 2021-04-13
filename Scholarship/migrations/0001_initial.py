# Generated by Django 3.1.7 on 2021-04-10 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Scholarship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('denomination', models.CharField(max_length=50)),
                ('referred_studies', models.CharField(max_length=50)),
                ('minimum_amount', models.IntegerField()),
                ('description', models.CharField(max_length=100)),
                ('criteria', models.CharField(max_length=100)),
            ],
        ),
    ]
