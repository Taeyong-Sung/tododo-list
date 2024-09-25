from django.db import models
from django.urls import reverse

class Todo(models.Model):
  name = models.CharField(max_length=100)
  description = models.TextField(max_length=250)

  def __str__(self):
    return self.name
  
  def get_absolute_url(self):
    return reverse('todo-detail', kwargs={'todo_id': self.id})