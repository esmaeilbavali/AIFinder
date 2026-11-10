from rest_framework import serializers

from apps.catalog.models import AITool

class ToolSerializer(serializers.ModelSerializer):

    categories = serializers.StringRelatedField(many=True)

    audiences = serializers.StringRelatedField(many=True)

    class Meta:
        model = AITool

        fields = [
            "id",
            "name",
            "slug",
            "description",
            "website_url",
            "pricing_type",
            "price_details",
            "features",
            "pros",
            "cons",
            "categories",
            "audiences",
            "image",
            "created_at",
            "updated_at",
        ]
        read_only_fields = fields
    
