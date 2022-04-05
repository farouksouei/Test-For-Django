from rest_framework import serializers
from . models import Posts


class PostSerializer(serializer.ModelSerializer):
    class Meta:
        model = Posts
        fields = '__all__'
