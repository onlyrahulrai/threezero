# Generated by Django 3.2.6 on 2021-09-09 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0002_alter_examdate_exam_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='examdate',
            name='exam_date',
            field=models.DateField(),
        ),
    ]