# Generated by Django 4.0.6 on 2022-08-11 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='whatsappdb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Contact', models.IntegerField(max_length=200)),
                ('name', models.CharField(max_length=200)),
                ('pdf', models.FileField(upload_to='specs')),
            ],
        ),
    ]
