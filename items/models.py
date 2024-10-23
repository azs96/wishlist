from django.db import models

# Create your models here.
class Item(models.Model):
  name = models.CharField(max_length=200)
  memo = models.TextField(null=True, blank=True)
  price = models.IntegerField(default=0) # todo minとmaxにする？

  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.name