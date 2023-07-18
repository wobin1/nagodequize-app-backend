from django.db import models


class Quize(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    quiz_score = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    test_status = models.CharField(max_length=200, default="pending")
    user_role = models.CharField(max_length=200, default="user")

    def __str__(self):
        return self.name

