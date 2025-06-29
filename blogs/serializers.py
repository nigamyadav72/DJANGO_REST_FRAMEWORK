from rest_framework import serializers
from blogs.models import Blog, Comment


class commentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"


class blogSerializer(serializers.ModelSerializer):
    comments = commentSerializer(many = True, read_only = True)
    class Meta:
        model = Blog
        fields = "__all__"


