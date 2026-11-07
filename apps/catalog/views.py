from django.views.generic import ListView, DetailView
from django.db.models import Q, Count

from .models import AITool
from apps.taxonomy.models import Category, Audience
from django.shortcuts import render, get_object_or_404

class HomeView(ListView):

    model = AITool
    template_name = "catalog/home.html"
    context_object_name = "tools"
    paginate_by = 9

    sort_options = {
        "newest": "-id",
        "oldest": "id",
        "name_asc": "name",
        "name_desc": "-name",
        "pricing": "pricing_type",
    }

    sort_choices = {
        ("newest", "Newest"),
        ("oldest", "Oldest"),
        ("name_asc", "Name (A-Z)"),
        ("name_desc", "Name (Z-A)"),
        ("pricing", "Pricing Type"),
    }

    def get_queryset(self):
        params = self.request.GET
        self.query = params.get("q", "").strip()
        self.category_id = params.get("category", "")
        self.audience_id = params.get("audience", "")
        self.pricing_type = params.get("pricing", "")
        self.sort_by = params.get("sort", "newest")

        # Validating Sorting option
        if self.sort_by not in self.sort_options:
            self.sort_by = "newest"

        # Base queryset
        queryset = AITool.objects.filter(
            is_active = True
        ).prefetch_related(
            "categories",
            "audiences"
        )

        # Search
        if self.query:
            queryset = queryset.filter(
                Q(name__icontains=self.query) |
                Q(description__icontains=self.query)
            )

        # Category filter
        if self.category_id:
            queryset = queryset.filter(
                categories__id=self.category_id
            )

        # Audience filter
        if self.audience_id:
            queryset = queryset.filter(
                audiences__id=self.audience_id
            )

        # Pricing filer
        if self.pricing_type:
            queryset = queryset.filter(
                pricing_type=self.pricing_type
            )

        # Remove duplicate result
        queryset = queryset.distinct()

        # Sorting
        queryset = queryset.order_by(
            self.sort_options[self.sort_by]
        )

        return queryset

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        # Pagination information
        page_obj = context["page_obj"]

        context["total_results"] = page_obj.paginator.count

        context["start_index"] = (
            page_obj.end_index()
            if page_obj.paginator.count else 0
        )

        # Preserve search and filter parameters
        query_params = self.request.GET.copy()
        query_params.pop("page", None)

        context["query_params"] = query_params.urlencode()

        # Search and filter values
        context["query"] = self.query

        context["selected_category"] = self.category_id
        context["selected_audience"] = self.audience_id
        context["selected_pricing"] = self.pricing_type

        # Sorting
        context["selected_sort"] = self.sort_by
        context["sort_options"] = self.sort_choices

        # Categories with active tool counts
        context["categories"] = Category.objects.annotate(
            tool_count = Count(
                "tools",
                filter=Q(tools__is_active=True),
                distinct=True
            )
        )

        # Audiences
        context["audiences"] = Audience.objects.all()

        # Pricing choices
        context["pricing_choices"] = (
            AITool._meta.get_field("pricing_type").choices
        )

        return context



    
class ToolDetailView(DetailView):

    model = AITool
    template_name = "catalog/tool_detail.html"
    context_object_name = "tool"
    slug_field = "slug"
    slug_url_kwarg = "slug"

    def get_queryset(self):

        return AITool.objects.filter(
            is_active=True
        ).prefetch_related(
            "categories",
            "audiences"
        )

class CategoryDetailView(ListView):

    model = AITool
    template_name = "catalog/category_detail.html"
    context_object_name = "tools"

    def get_queryset(self):
        self.category = get_object_or_404(
            Category,
            slug=self.kwargs["slug"]
        )

        return AITool.objects.filter(
            is_active=True,
            categories=self.category
        ).prefetch_related(
            "categories",
            "audiences"
        ).order_by("-id")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["category"] = self.category
        context["total_results"] = self.object_list.count()

        return context

class AudienceDetailView(ListView):
    model = AITool
    template_name = "catalog/audience_detail.html"
    context_object_name = "tools"

    def get_queryset(self):
        self.audience = get_object_or_404(
            Audience,
            slug=self.kwargs["slug"]
        )

        return AITool.objects.filter(
            is_active=True,
            audiences=self.audience
        ).prefetch_related(
            "categories",
            "audiences"
        ).order_by("-id")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["audience"] = self.audience
        context["total_results"] = self.object_list.count()

        return context