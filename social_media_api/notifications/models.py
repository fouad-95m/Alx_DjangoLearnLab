from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.conf import settings

class Notification(models.Model):
    recipient = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='notifications')
    actor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='actor_notifications')
    verb = models.CharField(max_length=255)  # Action description (e.g., "liked your post")
    target_ct = models.ForeignKey(ContentType, on_delete=models.CASCADE, blank=True, null=True)
    target_id = models.PositiveIntegerField(blank=True, null=True)
    target = GenericForeignKey('target_ct', 'target_id')
    created_at = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)  # Tracks if the notification has been read
    ["timestamp"]
