#coding:utf-8
from django.contrib import admin
from courses.models import Course
from training_areas.models import TrainingArea
from news.models import Notice
from carousel_items.models import CarouselItem

admin.site.register(Course)
admin.site.register(TrainingArea)
admin.site.register(Notice)
admin.site.register(CarouselItem)