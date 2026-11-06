from django.shortcuts import render, get_object_or_404
from django.db.models import Q, Count
from .models import AITool, Category, Audience
from django.core.paginator import Paginator
from apps.taxonomy.models import Category, Audience


def home(request):
    query = request.GET.get("q", "").strip()
    category_id = request.GET.get("category", "")
    audience_id = request.GET.get("audience", "")
    pricing_type = request.GET.get("pricing", "")
    sort_by = request.GET.get("sort", "newest")

    tools = AITool.objects.filter(
        is_active=True
    ).prefetch_related(
        "categories",
        "audiences"
    )

    # Search
    if query:
        tools = tools.filter(
            Q(name__icontains=query) |
            Q(description__icontains=query)
        )

    # Category filter
    if category_id:
        tools = tools.filter(
            categories__id=category_id
        )

    # Audience filter
    if audience_id:
        tools = tools.filter(
            audiences__id=audience_id
        )

    # Pricing filter
    if pricing_type:
        tools = tools.filter(
            pricing_type=pricing_type
        )

    tools = tools.distinct()

    # Sorting
    sort_options = {
        "newest": "-id",
        "oldest": "id",
        "name_asc": "name",
        "name_desc": "-name",
        "pricing": "pricing_type",
    }

    sort_by = sort_by if sort_by in sort_options else "newest"

    tools = tools.order_by(sort_options[sort_by])

    # Total number of filtered tools
    total_results = tools.count()

    # Pagination
    paginator = Paginator(tools, 9)

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    # Pagination information
    start_index = page_obj.start_index() if total_results else 0
    end_index = page_obj.end_index() if total_results else 0


    # Pagination
    paginator = Paginator(tools, 9)

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    # Preserve search and filter parameters
    query_params = request.GET.copy()
    query_params.pop("page", None)
    query_params = query_params.urlencode()

    categories = Category.objects.annotate(
        tool_count=Count(
            "tools",
            filter=Q(tools__is_active=True),
            distinct=True
        )
    )

    pricing_choices = AITool._meta.get_field("pricing_type").choices
    context = {
    "tools": page_obj,
    "page_obj": page_obj,
    "query_params": query_params,

    "query": query,
    "categories": categories,
    "audiences": Audience.objects.all(),
    "pricing_choices": pricing_choices,

    "selected_category": category_id,
    "selected_audience": audience_id,
    "selected_pricing": pricing_type,

    "total_results": total_results,
    "start_index": start_index,
    "end_index": end_index,

    "selected_sort": sort_by,
    "sort_options": [
        ("newest", "Newest"),
        ("oldest", "Oldest"),
        ("name_asc", "Name (A-Z)"),
        ("name_desc", "Name (Z-A)"),
        ("pricing", "Pricing Type"),
    ],
}

    return render(request, "catalog/home.html", context)


def tool_detail(request, slug):
    tool = get_object_or_404(
        AITool.objects.prefetch_related(
            "categories",
            "audiences"
        ),
        slug=slug,
        is_active=True
    )

    context = {"tool": tool}

    return render(request, "catalog/tool_detail.html", context)

def category_detail(request, slug):

    category = get_object_or_404(
        Category,
        slug=slug
    )

    tools = category.tools.filter(
        is_active=True
    ).prefetch_related(
        "categories",
        "audiences"
    ).order_by("-id")

    context = {
        "category": category,
        "tools": tools,
        "total_results": tools.count(),
    }

    return render(
        request,
        "catalog/category_detail.html",
        context
    )

def audience_detail(request, slug):

    audience = get_object_or_404(
        Audience,
        slug=slug
    )

    tools = audience.tools.filter(
        is_active=True
    ).prefetch_related(
        "categories",
        "audiences"
    ).order_by("-id")

    context = {
        "audience": audience,
        "tools": tools,
        "total_results": tools.count(),
    }

    return render(
        request,
        "catalog/audience_detail.html",
        context
    )