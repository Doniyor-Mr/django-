from django.db import models
from django.urls import reverse

class News(models.Model):
    title = models.CharField(max_length=150, verbose_name='text')
    contact = models.TextField(blank=True, verbose_name='matn')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='OZGARADI voqt')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='OZGARMIDI voqt')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='rasm', blank=True)
    is_published = models.BooleanField(default=True, verbose_name='HA/YOQ')
    category = models.ForeignKey('Category', on_delete=models.PROTECT,null=True, verbose_name='for categoriya')

    def get_absolute_url(self):
        return reverse('view_news', kwargs={'pk':self.pk})




    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "habar"  # iciga yoiladi adminkani
        verbose_name_plural = 'Habarlar'  # tashqarisiga yoziladi
        ordering = ['created_at']


class Category(models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name='kategoriya')


    def get_absolute_url(self):
        return reverse('category', kwargs={'category_id':self.pk})


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "kategoriya"  # iciga yoiladi adminkani
        verbose_name_plural = 'kategoriy'  # tashqarisiga yoziladi
