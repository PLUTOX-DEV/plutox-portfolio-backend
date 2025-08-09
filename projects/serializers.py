from rest_framework import serializers
from .models import Project

class ProjectSerializer(serializers.ModelSerializer):
    icon_names = serializers.ListField(
        child=serializers.CharField(), required=False
    )
    image = serializers.SerializerMethodField()  # ✅ Make image absolute URL

    class Meta:
        model = Project
        fields = [
            'id',
            'title',
            'slug',
            'description',
            'image',
            'live_url',
            'github_url',
            'icon_names',
        ]

    def get_image(self, obj):
        request = self.context.get('request')
        return request.build_absolute_uri(obj.image.url) if obj.image else None

    def to_internal_value(self, data):
        if hasattr(data, 'getlist'):
            data = data.copy()
            data.setlist('icon_names', data.getlist('icon_names'))
        return super().to_internal_value(data)
