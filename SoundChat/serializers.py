from rest_framework import serializers
from .models import Message

class MessageSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField()
    timestamp = serializers.SerializerMethodField()

    class Meta:
        model = Message
        fields = ['id', 'content', 'username', 'timestamp']

    def get_username(self, obj):
        return obj.user.username if obj.user else "Guest"

    def get_timestamp(self, obj):
        return obj.timestamp.strftime("%H:%M")