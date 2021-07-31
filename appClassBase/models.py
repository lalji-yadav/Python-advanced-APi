from django.db import models

# Create your models here.


class Tech(models.Model):

    owner = models.ForeignKey('auth.User', related_name='tech', on_delete=models.CASCADE)

    created = models.DateTimeField(auto_now_add=True)
    Address = models.CharField(max_length=100, blank=True, default='')
    code = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    mobile = models.IntegerField()

    class Meta:
        ordering = ['created']