# -*- coding: utf-8 -*-
from django.db import models

class Student (models.Model):
	"""Stedent Model"""
	class Meta(object):
		verbose_name = u"Студент"
		verbose_name_plural = u"Студенти"
	first_name = models.CharField(max_length=256, blank = False )
	last_name = models.CharField(max_length=256, blank= False, verbose_name=u"Прізвище")
	middle_name = models.CharField(max_length=256, blank = True, verbose_name=u"По-батькові", default="" )
	birthday = models.DateField(blank= False, verbose_name=u"Дата Народження", null= True)
	photo = models.ImageField(blank= True, verbose_name=u"Фото", null= True)
	ticket = models.CharField(max_length=256, blank=False, verbose_name=u"Білет")
	note = models.TextField(blank=True, verbose_name=u"Додаткові нотатки")

	def __unicode__(self):
		return u"%s %s" % (self.first_name, self.last_name)

