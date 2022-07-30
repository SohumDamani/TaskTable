from django.db import models

class Task(models.Model):

    priority_choices = (
        ('low','low'),
        ('high','high'),
        ('medium','medium'),
        ('urgent','urgent'),
    )
    status_choices = (
        ('Not Completed','Not Completed'),
        ('Completed','Completed')
        )

    title = models.CharField(max_length=250,unique=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    priority = models.CharField(max_length=20,choices=priority_choices,default='low')
    status =  models.CharField(max_length=20,choices=status_choices,default='Not Completed')

    def __str__(self):
        return self.title
