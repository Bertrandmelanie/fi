from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200, null=True)

    # explanation of items
    description = models.TextField(null=True, blank=True)
    # when task is completed
    complete = models.BooleanField(default=False)
    # When the task was created(date and time)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    class Reta:
        ordering = ['complete']


