from distutils.command.upload import upload
from django.db import models
from memberships.models import Membership
from django.contrib.auth.models import User
from django.urls import reverse

class Klasa(models.Model):
    Курстун_аты = models.CharField(max_length=150)
    Ачыктоо = models.TextField(max_length= 200, null=True)
    Сурот = models.ImageField(upload_to='cat_images', default='cat_images/1.jpg')

    def __str__(self):
        return '{}'.format(self.Курстун_аты)

class Lendet(models.Model):
    krijues = models.ForeignKey(User,on_delete = models.CASCADE)
    slug = models.SlugField()
    Курстун_аты = models.CharField(max_length=30)
    Класс = models.ForeignKey(Klasa,on_delete=models.CASCADE)
    Ачыктоо = models.TextField(max_length=400)
    krijuar_me = models.DateTimeField(auto_now=True)
    Сурот_туру = models.ImageField(upload_to='kurs_images', default='1.jpg')

    def __str__(self):
        return self.Курстун_аты

    def get_absolute_url(self):
        return reverse("courses:course_detail", kwargs={"slug": self.slug})

    def get_courses_related_to_memberships(self):
        return self.courses.all()

    @property
    def lessons(self):
        return self.lesson_set.all().order_by('Катары')




class Lesson(models.Model):
    slug = models.SlugField()
    Курстун_аты = models.CharField(max_length=30)
    Туру = models.ForeignKey(Lendet,on_delete=models.CASCADE)
    Материалы =  models.FileField(blank=True)
    Видео = models.FileField(upload_to='videos/', default='videos/1.mp4' )
    Катары = models.IntegerField()

    def __str__(self):
        return self.Курстун_аты

    def get_absolute_url(self):
        return reverse("courses:lesson_detail", kwargs={"course_slug": self.Туру.slug,'lesson_slug':self.slug})
