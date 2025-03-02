from django.db import models
from django.contrib.auth.models import User

class CodeReview(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    code_text = models.TextField()
    review_feedback = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review by {self.user.username} on {self.created_at.strftime('%Y-%m-%d %H:%M')}"
