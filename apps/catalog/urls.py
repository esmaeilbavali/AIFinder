from django.urls import path
from . import views


urlpatterns = [
    # path("", views.home, name="home"),
    path("", views.HomeView.as_view(), name="home"),

    path(
        "tools/<slug:slug>/",
        views.ToolDetailView.as_view(),
        name="tool_detail"
    ),
    path(
        "categories/<slug:slug>/",
        views.CategoryDetailView.as_view(),
        name="category_detail"
    ),
    path(
    "audiences/<slug:slug>/",
    views.AudienceDetailView.as_view(),
    name="audience_detail"
    ),
]