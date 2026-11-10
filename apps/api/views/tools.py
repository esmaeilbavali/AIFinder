from rest_framework import filters, generics
from rest_framework.permissions import AllowAny
from apps.api.filters import filter_tools

from apps.catalog.selectors import get_active_tools
from apps.api.serializers import ToolSerializer
from apps.api.serializers.filters import ToolFilterSerializer

class ToolListView(generics.ListAPIView):

    serializer_class = ToolSerializer

    permission_classes = [AllowAny]

    filter_backends = [
        filters.SearchFilter,
        filters.OrderingFilter
    ]

    search_fields = [
        "name",
        "description"
    ]

    ordering_fields = [
        "name",
        "pricing_type",
        "created_at",
        "updated_at"
    ]

    ordering = ["-id"]

    def get_queryset(self):

        params = {
        "category": self.request.query_params.get("category", ""),
        "audience": self.request.query_params.get("audience", ""),
        "pricing": self.request.query_params.get("pricing", ""),
        }

        filter_serializer = ToolFilterSerializer(data=params)
        filter_serializer.is_valid(raise_exception=True)

        queryset = get_active_tools()

        return filter_tools(
            queryset=queryset,
            **filter_serializer.validated_data
        )

class ToolDetailView(generics.RetrieveAPIView):

    serializer_class = ToolSerializer

    permission_classes = [AllowAny]

    lookup_field = "slug"

    def get_queryset(self):
        return get_active_tools()