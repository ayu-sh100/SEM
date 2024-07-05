from django.db import models

from app_customuser.models import CustomUser
class Assignment(models.Model):
        Name = models.CharField(default=None,max_length=50)
        Start_date = models.DateField(default=None)
        End_date = models.DateField(default=None)
        Created_by =models.ForeignKey(CustomUser, on_delete=models.SET_NULL,null=True)
        Summary = models.TextField(default=None)
        Tags = models.CharField(max_length=20,default=None)

        def __str__(self):
            return self.Name  

class AssignmentProgress(models.Model):
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.SET_NULL,null=True) 
    is_complete = models.BooleanField(default=False)
    percent_progress = models.PositiveIntegerField(default=0)
    score = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)

        