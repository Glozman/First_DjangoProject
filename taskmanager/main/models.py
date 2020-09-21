from django.db import models

class Task(models.Model):
    title = models.CharField('Name', max_length=30)
    task = models.TextField('Description')


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'План'
        verbose_name_plural = 'Планы'
