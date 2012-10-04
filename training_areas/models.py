#coding:utf-8
from django.db import models


class string_with_title(str):
    def __new__(cls, value, title):
        instance = str.__new__(cls, value)
        instance._title = title
        return instance
    def title(self):
        return self._title
    __copy__ = lambda self: self
    __deepcopy__ = lambda self, memodict: self

# Create your models here.
class TrainingArea(models.Model):
		des = models.CharField(max_length=120, verbose_name="Descrição")
		content = models.TextField(max_length=2000, verbose_name="Conteúdo")
		def __unicode__(self):
				return self.des
		class Meta:
				app_label = string_with_title("training_areas", "Areas de Treinamento")
				db_table = u'training_areas'
				verbose_name = 'Área de Treinamento'
				verbose_name_plural = 'Áreas de Treinamento'