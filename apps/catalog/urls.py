from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name="home"),

        path(
        "tools/<slug:slug>/",
        views.tool_detail,
        name="tool_detail"
        ),
        path(
            "categories/<slug:slug>/",
            views.category_detail,
            name="category_detail"
        ),
        path(
        "audiences/<slug:slug>/",
        views.audience_detail,
        name="audience_detail"
        ),
]