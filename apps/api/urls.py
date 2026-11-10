from django.urls import path
from apps.api.views import ToolListView, ToolDetailView

app_name = "api"

urlpatterns = [
    path("tools/", ToolListView.as_view(), name="tool-list"),
    path("tools/<slug:slug>", ToolDetailView.as_view(), name="tool-detail"),
]