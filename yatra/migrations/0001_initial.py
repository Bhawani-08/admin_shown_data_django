# Generated by Django 4.2.11 on 2024-04-02 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PersonalP',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('Address', models.CharField(max_length=30)),
                ('Phone', models.IntegerField()),
                ('Mobile', models.IntegerField()),
                ('E_mail', models.EmailField(max_length=254)),
                ('Aadhar_card', models.IntegerField()),
            ],
        ),
    ]
