from rest_framework import serializers
from ..travel.models import AttractionPost


class AttractionPostSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(read_only=True, slug_field="username")
    comments = serializers.PrimaryKeyRelatedField(read_only=True, many=True)
    total_comments  = serializers.IntegerField(read_only=True,)
    class Meta:
        model = AttractionPost
        fields = ['pk', 'user', 'title', 'country', 'description', 'created_at', 'interest_rating', 'comments', 'total_comments']
