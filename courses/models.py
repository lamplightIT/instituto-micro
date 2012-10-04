#coding:utf-8
from django.db import models

# Create your models here.
class Course(models.Model):
		des = models.CharField(max_length=120, verbose_name="Descrição")
		img = models.ImageField(upload_to='img/courses/')
		def __unicode__(self):
				return self.des
		class Meta:
				db_table = u'courses'
				verbose_name = 'curso'
				verbose_name_plural = 'cursos'