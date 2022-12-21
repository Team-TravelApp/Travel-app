from rest_framework import serializers
from travel.models import AttractionPost, Comment


class AttractionPostSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(read_only=True, slug_field="username")
    comments = serializers.PrimaryKeyRelatedField(read_only=True, many=True)
    total_comments  = serializers.IntegerField(read_only=True,)
    class Meta:
        model = AttractionPost
        fields = ['pk', 'user', 'title', 'country', 'description', 'created_at', 'interest_rating', 'comments', 'total_comments', 'image']

    def update(self, instance, validated_data):
        if "file" in self.initial_data:
            file = self.initial_data.get("file")
            instance.image.save(file.name, file, save=True)
            return instance
        # this call to super is to make sure that update still works for other fields
        return super().update(instance, validated_data)


class CommentSerializer(serializers.ModelSerializer):
    comment_owner = serializers.SlugRelatedField(read_only=True, slug_field="username")
    attractionpost = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = Comment
        fields = ['pk', 'comment_owner', 'attractionpost', 'commenttext', 'created_at']

