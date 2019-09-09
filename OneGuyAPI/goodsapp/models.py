from django.db import models
from common import YGBaseModel
<<<<<<< HEAD

=======
from userapp.models import OneGuoUser
>>>>>>> ccd5ad33554c515af07a39a225123d3c011d3b57
# Create your models here.
class GoodsModelEntity(models.Model):
    goods_type = models.IntegerField(verbose_name='商品分类')
    goods_type_info = models.CharField(max_length=20,verbose_name='分类详情')
    goods_name= models.CharField(max_length=10,verbose_name='商品名称')
    goods_info = models.CharField(max_length=50,verbose_name='商品描述')
    goods_price= models.DecimalField(max_digits=10,
                                     decimal_places=2,
                                     verbose_name='商品价格')
    super_price = models.DecimalField(max_digits=10,
                                      decimal_places=2,
                                      verbose_name='市场价格')
    product_address = models.CharField(max_length=30,verbose_name='原产地')
    info_page= models.ImageField(upload_to='goods',
                                 verbose_name='详情页图片')
    goods_sale = models.IntegerField(verbose_name='销量')
    goods_have = models.IntegerField(verbose_name='库存')
    info_id = models.IntegerField(verbose_name='详情id')
    type_id = models.IntegerField(verbose_name='分类id')
    goods_img= models.ImageField(upload_to='goods',verbose_name='商品图片')
    is_detail = models.BooleanField(choices=((0,'是'),(1,'否')),
                                    verbose_name='是否精选图片')

    def __str__(self):
        return self.goods_name

    class Meta:
        db_table = 't_goods'
        verbose_name_plural = verbose_name = '商品表'

class Goods_cartModelEntity(models.Model):
    user_id = models.OneToOneField(OneGuoUser,verbose_name='用户id',on_delete=models.CASCADE)
    goods_id = models.ForeignKey(GoodsModelEntity,
                                 on_delete=models.CASCADE,
                                 verbose_name='商品id')
    goods_count = models.IntegerField(verbose_name='商品数量')
    is_choice = models.BooleanField(choices=((0,'True'),(1,'False')),
                                    verbose_name='是否选中')
    def __str__(self):
        return self.user_id

    class Meta:
        db_table = 't_goods_cart'
        verbose_name_plural = verbose_name = '购物车表'

class Category(YGBaseModel):
    code = models.CharField(max_length=20,
                            verbose_name='编码')
    name = models.CharField(max_length=20,
                            verbose_name='名称')
    grade = models.IntegerField(default=1,
                                verbose_name='等级')
    parent = models.ForeignKey('self',
                               on_delete=models.CASCADE,
                               verbose_name='父类',
                               null=True,
                               blank=True)
    picture_url = models.CharField(max_length=200,
                                   verbose_name='图片路径',
                                   blank=True,
                                   null=True)
    def __str__(self):
        return self.name

    class Meta:
        db_table = 't_category'
        verbose_name = verbose_name_plural = '分类表'










