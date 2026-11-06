from django.contrib import admin
from .models import Category, Audience


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")
    search_fields = ("name",)


@admin.register(Audience)
class AudienceAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")
    search_fields = ("name",)