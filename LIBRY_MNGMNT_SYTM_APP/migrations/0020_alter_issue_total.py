# Generated by Django 3.2.15 on 2022-10-13 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LIBRY_MNGMNT_SYTM_APP', '0019_alter_issue_penalty'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issue',
            name='total',
            field=models.IntegerField(blank=True),
        ),
    ]