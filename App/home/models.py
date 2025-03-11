from django.db import models

class NewTask(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(default='Default description')
    completed = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title
