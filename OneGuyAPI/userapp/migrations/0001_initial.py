# Generated by Django 2.0.1 on 2019-09-09 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OneGuoAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField(verbose_name='用户id')),
                ('user_addr', models.CharField(max_length=200, verbose_name='用户地址')),
                ('addr_state', models.IntegerField(choices=[(0, '公司地址'), (1, '家庭地址')], default=0, verbose_name='地址状态')),
                ('user_name', models.CharField(max_length=20, verbose_name='收件人')),
                ('phone', models.IntegerField(verbose_name='联系电话')),
            ],
            options={
                'verbose_name': '收货地址',
                'verbose_name_plural': '收货地址',
                'db_table': 'OneGuoAddress',
            },
        ),
        migrations.CreateModel(
            name='OneGuoUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=30, null=True, verbose_name='手机号')),
                ('name', models.CharField(max_length=20, null=True, verbose_name='昵称')),
                ('gender', models.CharField(choices=[('man', '男'), ('woman', '女')], default='woman', max_length=10, null=True, verbose_name='性别')),
                ('password', models.CharField(max_length=20, null=True, verbose_name='用户密码')),
                ('idcard', models.CharField(max_length=20, null=True, verbose_name='身份证')),
                ('img', models.ImageField(blank=True, null=True, upload_to='img/%Y/%m/%d', verbose_name='用户头像')),
                ('balance', models.FloatField(default=0.0, null=True, verbose_name='账户余额')),
                ('use_level', models.CharField(choices=[('0', '大众会员'), ('1', '白银会员'), ('2', '黄金会员'), ('3', '钻石会员')], default=0, max_length=20, null=True, verbose_name='用户等级')),
                ('is_active', models.BooleanField(default=False, verbose_name='是否激活')),
                ('is_delete', models.BooleanField(default=False, verbose_name='是否删除')),
            ],
            options={
                'verbose_name': '用户表',
                'verbose_name_plural': '用户表',
                'db_table': 'users',
            },
        ),
    ]
