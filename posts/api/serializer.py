from rest_framework import serializers
from posts.models import BlogPost

class BlogPostSerializer(serializers.ModelSerializer):
    url      = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = BlogPost
        fields = [
            'url',
            'id',
            'user',
            'title',
            'content',
            'timestamp'
        ]
        read_only_fields=['user']

    def get_url(self, obj):
        request = self.context.get("request")
        return obj.get_api_url(request=request)

    def validate_title(self, value):
        qs = BlogPost.objects.filter(title__iexact = value)
        if self.instance:
            qs=qs.exclude(id=self.instance.id)
        if qs.exists():
            raise serializers.ValidationError("Title should be unique")
        return value