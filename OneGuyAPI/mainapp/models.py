from django.db import models


# Create your models here.
class OneGuoCity(models.Model):
    hot = ((0, '热门'), (1, '非热门'))
    id = models.IntegerField(max_length=20, verbose_name='城市id', primary_key=True)
    city_name = models.CharField(max_length=60, verbose_name='城市名称')
    is_hot = models.CharField(max_length=10, verbose_name='是否热门', choices=hot, default=1)
    py_name = models.CharField(max_length=50, verbose_name='城市拼音名')

    def __str__(self):
        return self.city_name

    class Meta:
        db_table = 'OneGuoCity'
        verbose_name_plural = verbose_name = '全国各大城市'
