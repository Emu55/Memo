from rest_framework import serializers
from .models import Memo

class MemoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Memo  # Specify model to be serialized
        fields = '__all__'  # Only 'message' field


