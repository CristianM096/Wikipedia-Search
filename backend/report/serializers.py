from rest_framework import serializers
from .models import Query
from .models import Result

class QuerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Query
        fields = ('id', 'title', 'created_at')