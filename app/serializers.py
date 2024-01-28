# serializers.py
from rest_framework import serializers


# serializer data for result tasks
class CeleryTaskResultSerializer(serializers.Serializer):
    task_id = serializers.CharField(max_length=255)
    result = serializers.JSONField()

