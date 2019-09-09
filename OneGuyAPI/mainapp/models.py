from django.db import models


# Create your models here.
class address(models.Model):
    state = ((0, '公司地址'), (1, '家庭地址'))
    user_id = models.IntegerField(max_length=50, verbose_name='用户id')
    user_addr = models.CharField(max_length=200, verbose_name='用户地址')
    addr_state = models.IntegerField(verbose_name='地址状态', choices=state, default=0)
    user_name = models.CharField(max_length=20, verbose_name='收件人', null=False)
    phone = models.IntegerField(max_length=20, verbose_name='联系电话', null=False)

    class Meta:
        db_table = 'address'
        verbose_name_plural = verbose_name = '收货地址'


class city(models.Model):
    hot = ((0, '热门'), (1, '非热门'))
    id = models.IntegerField(max_length=20, verbose_name='城市id')
    city_name = models.CharField(max_length=60, verbose_name='城市名称')
    is_hot = models.CharField(verbose_name='是否热门', choices=hot, default=1)
    py_name = models.CharField(max_length=50, verbose_name='城市拼音名')

    class Meta:
        db_table = 'city'
        verbose_name_plural = verbose_name = '全国各大城市'