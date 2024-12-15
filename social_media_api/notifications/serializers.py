from rest_framework import serializers
from .models import Notification

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = ['id', 'recipient', 'actor', 'verb', 'target', 'created_at', 'read']
        read_only_fields = ['id', 'recipient', 'actor', 'verb', 'target', 'created_at']