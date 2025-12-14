from django.db import models
from django.conf import settings

from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType


from accounts.models import CustomUser


# Create your models here.
class Notification(models.Model):
    recipient = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="received_notifications")
    actor = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="sent_notifications")
    verb = models.TextField()
    target_content_type = models.ForeignKey(
        ContentType,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    target_object_id = models.PositiveIntegerField(null=True, blank=True)
    target = GenericForeignKey("target_content_type", "target_object_id")

    timestamp = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    class Meta:
        ordering = ["-timestamp"]

    def __str__(self):
        return f"{self.actor} {self.verb} → {self.recipient}"
    timestamp = models.DateTimeField(auto_now_add=True)