from django.db import models

from student.choices import StatusChoices
from student.mixins import BasicTimeStamp

# Create your models here.


class Task(BasicTimeStamp):
    title = models.CharField(null=True,blank=True,max_length=150)
    description = models.TextField(null=True,blank=True)
    status = models.CharField(max_length=20, choices=StatusChoices, default = StatusChoices.PENDING)
    
    class Meta:
        verbose_name = ('Task')
        verbose_name_plural = ('Tasks')

    def __str__(self):
        return f'{self.title}'