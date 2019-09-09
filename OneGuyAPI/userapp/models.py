from django.db import models

# Create your models here.
from .helper import make_password


class OneGuoUser(models.Model):
    level = (('0', '大众会员'),
             ('1', '白银会员'),
             ('2', '黄金会员'),
             ('3', '钻石会员'))
    sex = (('man', '男'),
           ('woman', '女'))
    phone = models.CharField(max_length=30,
                             verbose_name='手机号',
                             null=True)
    name = models.CharField(max_length=20,
                            verbose_name='昵称',
                            null=True)
    gender = models.CharField(max_length=10,
                              verbose_name='性别',
                              choices=sex,
                              default='woman',
                              null=True)  # 默认女 True 男 False
    password = models.CharField(max_length=20,
                                verbose_name='用户密码',
                                null=True)
    idcard = models.CharField(max_length=20,
                              verbose_name='身份证',
                              null=True)
    img = models.ImageField(upload_to='img/%Y/%m/%d',
                            verbose_name='用户头像',
                            null=True,
                            blank=True)
    balance = models.FloatField(verbose_name='账户余额',
                                default=0.0,
                                null=True)
    use_level = models.CharField(max_length=20,
                                 choices=level,
                                 verbose_name='用户等级',
                                 default=0,
                                 null=True)
    is_active = models.BooleanField(verbose_name='是否激活',
                                    default=False)
    is_delete = models.BooleanField(verbose_name='是否删除',
                                    default=False)

    def __str__(self):
        return self.name

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if len(self.password) < 20:
            self.password = make_password(self.password)
        super().save()

    class Meta:
        db_table = 'users'
        verbose_name = '用户表'
        verbose_name_plural = verbose_name


class OneGuoAddress(models.Model):
    state = ((0, '公司地址'), (1, '家庭地址'))

    user_id = models.OneToOneField(OneGuoUser,
                                   on_delete=models.CASCADE,
                                   verbose_name='用户id')
    user_addr = models.CharField(max_length=200, verbose_name='用户地址')
    addr_state = models.IntegerField(verbose_name='地址状态', choices=state, default=0)
    user_name = models.CharField(max_length=20, verbose_name='收件人', null=False)
    phone = models.IntegerField(verbose_name='联系电话', null=False)

    def __str__(self):
        return self.user_addr

    class Meta:
        db_table = 'OneGuoAddress'
        verbose_name_plural = verbose_name = '收货地址'
