from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=200)  # Task title
    description = models.TextField()  # Task description
    deadline = models.DateField()  # Task deadline
    created_at = models.DateTimeField(auto_now_add=True)  # Auto set when task is created
    task_id = models.CharField(max_length=255, unique=True, default="default_task_id")  # Adding default value
    price = models.IntegerField(default=0)
    
    payment_status = models.DecimalField(max_digits=10, decimal_places=2, default=False)  # Field for filling payment after task application
    



    def __str__(self):
        return self.title


