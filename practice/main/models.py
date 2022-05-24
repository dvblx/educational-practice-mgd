from django.db import models
from django.urls import reverse


class Evtype(models.Model):
    name_t = models.CharField('Тип мероприятия', max_length=20)

    def __str__(self):
        return self.name_t


class Event(models.Model):
    name_e = models.CharField('Название мероприятия', max_length=20)
    about = models.TextField('Описание', blank=True)
    time = models.DateTimeField(verbose_name='Время проведения')
    evtype = models.ForeignKey(Evtype, on_delete=models.PROTECT, verbose_name='Тип мероприятия')
    is_ok = models.BooleanField('Опубликовать', default=False)

    def __str__(self):
        return self.name_e

    def get_absolute_url(self):
        return reverse('event_info', kwargs={'event_id': self.pk})


class Skills(models.Model):
    name_s = models.CharField('Специализация', max_length=30)

    def __str__(self):
        return self.name_s


class UserCard(models.Model):
    name_u = models.CharField('Имя', max_length=20)
    surname_u = models.CharField('Фамилия', max_length=20)
    link = models.CharField('Связь со мной', max_length=30)
    skill = models.ForeignKey(Skills, on_delete=models.PROTECT, verbose_name='Специализация')

    def __str__(self):
        return self.name_u

