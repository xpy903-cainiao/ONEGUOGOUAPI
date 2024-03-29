from django.db import models

# Create your models here.
from userapp.models import OneGuoUser, OneGuoAddress
from goodsapp.models import GoodsModelEntity

class OrderModel(models.Model):
    order_STATE = ((0, '下单未付款'),
                   (1, '待收货'),
                   (2, '待评论'))
    order_id = models.CharField(max_length=20,primary_key=True ,verbose_name='订单ID')
    order_user_id = models.ForeignKey(OneGuoUser, on_delete=models.CASCADE, verbose_name='用户ID')
    order_price = models.FloatField(verbose_name='总价格')
    order_time = models.DateTimeField(auto_now=True, verbose_name='下单时间')
    order_state = models.IntegerField(choices=order_STATE, default=0, verbose_name='订单状态')
    address_id = models.ForeignKey(OneGuoAddress, on_delete=models.CASCADE, verbose_name='地址ID')

    def __str__(self):
        return self.order_id

    class Meta:
        db_table = 'Order'
        verbose_name_plural = verbose_name = '订单'


class OrderDetailModel(models.Model):
    order_id = models.ForeignKey(OrderModel, on_delete=models.CASCADE, verbose_name='订单ID')
    order_goods_id = models.ForeignKey(GoodsModelEntity,
                                       default=1,
                                       on_delete=models.CASCADE, verbose_name='商品ID')
    order_goods_num = models.IntegerField(default=1, verbose_name='商品数量')

    class Meta:
        db_table = 'OrderDetail'
        verbose_name_plural = verbose_name = '订单详情'

    def __str__(self):
        return '订单详情'


class OneGuoComment(models.Model):
    user_id = models.ForeignKey(OneGuoUser,
                                on_delete=models.CASCADE,
                                verbose_name='用户ID')
    order_id = models.ForeignKey(OrderModel,
                                 on_delete=models.CASCADE,
                                 verbose_name='订单ID')
    comments = models.CharField(max_length=500,
                                verbose_name='用户评论')
    class Meta:
        db_table = 'comments'
        verbose_name = '用户评论'
        verbose_name_plural = verbose_name