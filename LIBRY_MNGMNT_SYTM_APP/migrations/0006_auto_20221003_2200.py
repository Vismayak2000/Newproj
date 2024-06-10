# Generated by Django 3.2.15 on 2022-10-03 16:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('LIBRY_MNGMNT_SYTM_APP', '0005_auto_20221003_2146'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.TextField(blank=True)),
                ('Author', models.CharField(max_length=255)),
                ('available', models.BooleanField(default=True)),
                ('stock', models.IntegerField()),
                ('desc', models.CharField(max_length=255)),
                ('year', models.IntegerField()),
                ('language', models.CharField(max_length=255)),
                ('price', models.IntegerField()),
                ('Photo', models.ImageField(blank=True, null=True, upload_to='image/')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='LIBRY_MNGMNT_SYTM_APP.category')),
            ],
        ),
        migrations.DeleteModel(
            name='Books',
        ),
    ]
