from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from django.conf import settings





class User(AbstractUser):
    STUDENT = 'student'
    LECTURER = 'lecturer'
    DEPARTMENT_HEAD = 'department_head'
    ACADEMIC_REGISTRAR = 'academic_registrar'

    ROLE_CHOICES = [
        (STUDENT, 'Student'),
        (LECTURER, 'Lecturer'),
        (DEPARTMENT_HEAD, 'Department Head'),
        (ACADEMIC_REGISTRAR, 'Academic Registrar'),
    ]

    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default=STUDENT)

    def __str__(self):
        return f"{self.username} - {self.get_role_display()}"



class Issue(models.Model):
    ISSUE_TYPES = [
        ('MISSING_MARKS', 'Missing Marks'),
        ('APPEAL', 'Appeal'),
        ('CORRECTION', 'Correction'),
        ('OTHER', 'Other'),
    ]

    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('IN_PROGRESS', 'In Progress'),
        ('RESOLVED', 'Resolved'),
        ('CLOSED', 'Closed'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    issue_type = models.CharField(max_length=20, choices=ISSUE_TYPES)
    course_code = models.CharField(max_length=20)
    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='issues')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING')
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.issue_type} - {self.title}"

class Comment(models.Model):
    issue = models.ForeignKey(Issue, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Comment by {self.user.username} on {self.issue.title}"

class Notification(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='notifications')
    issue = models.ForeignKey(Issue, on_delete=models.CASCADE)
    message = models.CharField(max_length=255)
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Notification for {self.user.username}: {self.message}"