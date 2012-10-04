#coding:utf-8
from django.db import models

# Create your models here.
class CarouselItem(models.Model):
		img = models.ImageField(upload_to='img/carousel/')
		caption = models.CharField(max_length=70)
		def __unicode__(self):
				return self.caption
		class Meta:
				db_table = u'carousel_items'
				verbose_name = 'Imagem do Slider'
				verbose_name_plural = 'Imagens do Slider'