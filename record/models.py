from django.db import models
from django.contrib.auth.models import User

class StudentAssessmentRecord(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name="grades")
    score = models.IntegerField()
    
    def __str__(self):
        return f"{self.student.username}-Score:{self.score}"
    