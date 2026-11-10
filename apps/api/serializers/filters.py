from rest_framework import serializers

from apps.catalog.models import AITool
from apps.taxonomy.models import Category, Audience


class ToolFilterSerializer(serializers.Serializer):

    category = serializers.SlugField(
        required=False,
        allow_blank=True
    )

    audience = serializers.SlugField(
        required=False,
        allow_blank=True
    )

    pricing = serializers.ChoiceField(
        choices=AITool.PRICING_CHOICES,
        required=False,
        allow_blank=True,
    )

    def validate_category(self, value):
        if value and not Category.objects.filter(slug=value).exists():
            raise serializers.ValidationError(
                "Category does not exist."
            )

        return value

    def validate_audience(self, value):
        if value and not Audience.objects.filter(slug=value).exists():
            raise serializers.ValidationError(
                "Audience does not exist."
            )

        return value