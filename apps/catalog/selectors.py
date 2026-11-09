from django.db.models import Q
from .models import AITool
from apps.taxonomy.models import Category, Audience
from django.shortcuts import get_object_or_404

def get_active_tools():
    return AITool.objects.filter(
        is_active=True
    ).prefetch_related(
        "categories",
        "audiences"
    )

def search_tools(
    query = "",
    category_id ="",
    audience_id = "",
    pricing_type = "",
    sort_by = "-id",
    ):
    
    query_set = get_active_tools()

    if query:
        query_set = query_set.filter(
            Q(name__icontains = query) |
            Q(description__icontains = query)
        )
    
    if category_id:
        query_set = query_set.filter(
            categories__id = category_id
        )
    if audience_id:
        query_set = query_set.filter(
            audiences__id = audience_id
        )
    if pricing_type:
        query_set.filter(
            pricing_type = pricing_type
        )
    
    return query_set.distinct().order_by(sort_by)

def get_category_by_slug(slug):
    return get_object_or_404(
        Category,
        slug=slug
    )

def get_audience_by_slug(slug):
    return get_object_or_404(
        Audience,
        slug=slug
    )

def get_tools_by_category(category):
    return AITool.objects.filter(
        is_active = True,
        categories = category
    ).prefetch_related(
        "categories",
        "audiences"
    ).order_by("-id")

def get_tools_by_audience(audience):
    return AITool.objects.filter(
        is_active = True,
        audiences = audience
    ).prefetch_related(
        "categories",
        "audiences"
    ).order_by("-id")