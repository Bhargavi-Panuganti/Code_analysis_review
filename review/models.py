from django.db import models
from django.contrib.auth.models import User

class CodeReview(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    file_name = models.CharField(max_length=255,default="Untitled")
    code_content = models.TextField()
    review_feedback = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.file_name}"
