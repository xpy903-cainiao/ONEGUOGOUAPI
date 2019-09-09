from django.db import models


# Create your models here.
class OneGuoCity(models.Model):
    hot = ((0, '热门'), (1, '非热门'))
    city_id = models.IntegerField(verbose_name='城市id', primary_key=True)
    city_name = models.CharField(max_length=60, verbose_name='城市名称')
    is_hot = models.CharField(max_length=10, verbose_name='是否热门', choices=hot, default=1)
    py_name = models.CharField(max_length=50, verbose_name='城市拼音名')

    class Meta:
        db_table = 't_city'
        verbose_name_plural = verbose_name = '城市'

    def __str__(self):
        return self.city_name


class Navigationmodel(models.Model):
    Navigation_img1 = models.ImageField(verbose_name='导航图片',
                                        upload_to='goods', blank=True, null=True)
    Navigation_name = models.CharField(max_length=50,
                                       verbose_name='导航名称')
    Navigation_id = models.IntegerField(verbose_name='导航图片ID', )

    class Meta:
        db_table = 't_naviration'
        verbose_name_plural = verbose_name = '导航'

    def __str__(self):
        return self.Navigation_name


class NavigationInfomodel(models.Model):
    NavigationInfo_img1 = models.ImageField(verbose_name='导航详情图片',
                                            upload_to='goods')
    NavigationInfo_name = models.CharField(max_length=50,
                                           verbose_name='导航详情名称')
    NavigationInfo_id = models.IntegerField(verbose_name='导航详情图片ID', )
    user_id = models.CharField(max_length=30,
                               verbose_name='用户ID')

    def __str__(self):
        return self.NavigationInfo_name

    class Meta:
        db_table = 't_naviration_info'
        verbose_name_plural = verbose_name = '导航详情'
