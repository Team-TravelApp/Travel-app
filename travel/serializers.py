from rest_framework import serializers
from .models import AttractionPost


class AttractionPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = AttractionPost
        fields = ('pk', 'user', 'title', 'country', 'description', 'created_at', 'interest_rating')
