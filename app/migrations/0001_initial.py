# Generated by Django 2.0 on 2019-01-02 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=10)),
                ('label', models.CharField(max_length=50)),
                ('post_box', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Study',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('serial_number', models.CharField(help_text='Entrez un matricule sous le format 00A0000AA', max_length=20)),
                ('school', models.ManyToManyField(related_name='studies', to='app.School')),
            ],
        ),
    ]