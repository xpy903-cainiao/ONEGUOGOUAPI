# Generated by Django 2.0.1 on 2019-09-09 10:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='navigationinfomodel',
            options={'verbose_name': '导航详情', 'verbose_name_plural': '导航详情'},
        ),
        migrations.AlterModelTable(
            name='navigationinfomodel',
            table='t_naviration_info',
        ),
    ]