from django.urls import path
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
    SpectacularRedocView
)

from apps.api.views import ToolListView, ToolDetailView

app_name = "api"

urlpatterns = [
    path("tools/", ToolListView.as_view(), name="tool-list"),
    path("tools/<slug:slug>", ToolDetailView.as_view(), name="tool-detail"),

    # API documentation
    path("schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "docs/",
        SpectacularSwaggerView.as_view(url_name="api:schema"),
        name="swagger-ui",
    ),
    path(
        "redoc/",
        SpectacularRedocView.as_view(url_name="api:schema"),
        name="redoc"
    )
]