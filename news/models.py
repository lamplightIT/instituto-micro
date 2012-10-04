#coding:utf-8
from django.db import models

# Create your models here.
class Notice(models.Model):
		des = models.CharField(max_length=120, verbose_name="Descrição")
		content = models.TextField(max_length=2000, verbose_name="Conteúdo")
		date_pub = models.DateTimeField()
		def __unicode__(self):
				return self.des
		class Meta:
				db_table = u'news'
				verbose_name = 'Notícia'
				verbose_name_plural = 'Notícias'