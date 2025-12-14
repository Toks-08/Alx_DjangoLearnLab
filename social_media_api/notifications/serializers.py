from rest_framework import serializers

from notifications.models import Notification


class NotificationSerializer(serializers.ModelSerializer):
    actor = serializers.StringRelatedField()
    target = serializers.SerializerMethodField()

    class Meta:
        model = Notification
        fields = [
            "id",
            "actor",
            "verb",
            "target",
            "is_read",
            "timestamp",
        ]

    def get_target(self, obj):
        """
        Return a safe, minimal representation of the target object.
        """
        if not obj.target:
            return None

        return {
            "type": obj.target._meta.model_name,
            "id": obj.target.id,
            "str": str(obj.target),
        }