# Generated by Django 4.1.3 on 2023-03-15 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_rename_procedure_and_time_limits_procedure_and_time_limits_file'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rights_and_obligations_of_citizens_in_the_implementation_of_administrative_procedures',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Название')),
                ('file', models.FileField(upload_to='Procedure_and_time_limits/', verbose_name='Файл')),
                ('times', models.DateField(verbose_name='Дата публикации')),
            ],
            options={
                'verbose_name': 'Права и обязанности граждан при осуществлении административных процедур',
                'verbose_name_plural': 'Права и обязанности граждан при осуществлении административных процедур',
            },
        ),
    ]
