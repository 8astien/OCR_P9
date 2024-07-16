from django.db import models
from django.conf import settings


class UserFollows(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="following", on_delete=models.CASCADE)
    followed_user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="followed_by", on_delete=models.CASCADE)

    class Meta:
        unique_together = ("user", "followed_user")
        verbose_name = "User Follow"
        verbose_name_plural = "User Follows"

    def __str__(self):
        return f"{self.user.username} is following {self.followed_user.username}"
