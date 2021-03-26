from rest_framework import serializers

from msg.models import Message

class MessageListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['header', 'body', 'delivered_flag', 'read_flag', 'created_at', 'updated_at']

class MessageDetailSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Message
        fields = "__all__"