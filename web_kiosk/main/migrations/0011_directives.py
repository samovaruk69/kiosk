# Generated by Django 4.1.3 on 2023-04-26 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_document_forms'),
    ]

    operations = [
        migrations.CreateModel(
            name='Directives',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Название')),
                ('file', models.FileField(upload_to='Directives/', verbose_name='Файл')),
                ('times', models.DateField(verbose_name='Дата публикации')),
            ],
            options={
                'verbose_name': 'Директивы ',
                'verbose_name_plural': 'Директивы ',
            },
        ),
    ]
