from django.db import models

# Create your models here.


class Student(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    code = models.TextField()
    name = models.TextField()
    mobile = models.IntegerField()

    class Meta:
        ordering = ['created']