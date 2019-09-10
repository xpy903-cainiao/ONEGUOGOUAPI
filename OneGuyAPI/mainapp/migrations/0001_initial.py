# Generated by Django 2.0.1 on 2019-09-10 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NavigationInfomodel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NavigationInfo_img1', models.ImageField(upload_to='goods', verbose_name='导航详情图片')),
                ('NavigationInfo_name', models.CharField(max_length=50, verbose_name='导航详情名称')),
                ('NavigationInfo_id', models.IntegerField(verbose_name='导航详情图片ID')),
                ('user_id', models.CharField(max_length=30, verbose_name='用户ID')),
            ],
            options={
                'verbose_name': '导航详情',
                'verbose_name_plural': '导航详情',
                'db_table': 't_naviration_info',
            },
        ),
        migrations.CreateModel(
            name='Navigationmodel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Navigation_img1', models.ImageField(blank=True, null=True, upload_to='goods', verbose_name='导航图片')),
                ('Navigation_name', models.CharField(max_length=50, verbose_name='导航名称')),
                ('Navigation_id', models.IntegerField(verbose_name='导航图片ID')),
            ],
            options={
                'verbose_name': '导航',
                'verbose_name_plural': '导航',
                'db_table': 't_naviration',
            },
        ),
        migrations.CreateModel(
            name='OneGuoCity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_id', models.IntegerField(verbose_name='城市id')),
                ('city_name', models.CharField(max_length=60, verbose_name='城市名称')),
                ('is_hot', models.IntegerField(choices=[(0, '热门'), (1, '非热门')], default=1, verbose_name='是否热门')),
                ('py_name', models.CharField(max_length=50, verbose_name='城市拼音名')),
            ],
            options={
                'verbose_name': '城市',
                'verbose_name_plural': '城市',
                'db_table': 't_city',
            },
        ),
    ]
