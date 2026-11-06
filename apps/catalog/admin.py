from django.contrib import admin
from .models import AITool

# Register your models here.


@admin.register(AITool)
class AIToolAdmin(admin.ModelAdmin):
    list_display = ("name", "pricing_type", "is_active", "created_at")

    list_filter = ("pricing_type", "is_active", "categories")

    search_fields = ("name", "description")

    prepopulated_fields = {"slug": ("name",)}
