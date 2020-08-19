from django.db import models


TARH = (
    ('ساده', 'ساده'),
    ('طرح دار', 'طرح دار')
)

FORM = (
    ('معمولی', 'معمولی'),
    ('آزاد', 'آزاد')
)

STATUS_KOLAH = (
    ('بدون کلاه', 'بدون کلاه'),
    ('کلاهدار', 'کلاهدار')
)


class Size(models.Model):
    class Meta:
        verbose_name = 'سایز'
        verbose_name_plural = 'سایز'

    size = models.CharField(max_length=5, verbose_name='تعریف سایز')

    def __str__(self):
        return self.size


class SportSet(models.Model):
    class Meta:
        verbose_name = 'ست گرمکن و شلوار ورزشی'
        verbose_name_plural = 'ست گرمکن و شلوار ورزشی'

    name = models.CharField(max_length=100, verbose_name='نام')
    brand = models.CharField(max_length=50, verbose_name='برند')
    jens = models.CharField(max_length=50, verbose_name='جنس پارچه')
    tarh = models.CharField(max_length=7, choices=TARH, verbose_name='طرح پارچه')
    form = models.CharField(max_length=6, choices=FORM, verbose_name='فرم لباس')
    kolah = models.CharField(max_length=9, choices=STATUS_KOLAH, verbose_name='کلاه')
    size = models.ManyToManyField(Size, verbose_name='سایز')
    price = models.IntegerField(verbose_name='قیمت')
    inventory = models.IntegerField(default=0, verbose_name='تعداد موجودی')
    pic = models.ImageField(upload_to='SportSet', verbose_name='تصویر')
    pic1 = models.ImageField(upload_to='SportSet', verbose_name='تصویر', blank=True)
    pic2 = models.ImageField(upload_to='SportSet', verbose_name='تصویر', blank=True)
    pic3 = models.ImageField(upload_to='SportSet', verbose_name='تصویر', blank=True)
    pic4 = models.ImageField(upload_to='SportSet', verbose_name='تصویر', blank=True)

    def __str__(self):
        return self.name
