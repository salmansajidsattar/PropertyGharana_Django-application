# Generated by Django 2.2.2 on 2023-04-04 20:26

from django.db import migrations, models
import djrichtextfield.models


class Migration(migrations.Migration):

    dependencies = [
        ('mycompany', '0003_auto_20230405_0121'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', djrichtextfield.models.RichTextField()),
            ],
        ),
    ]
