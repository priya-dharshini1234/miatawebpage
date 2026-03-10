from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    ROLE_CHOICES = (
        ('student', 'Student'),
        ('agent', 'Agent'),
        ('professor', 'Professor'),
    )

    role = models.CharField(max_length=20, choices=ROLE_CHOICES,default="student")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username
