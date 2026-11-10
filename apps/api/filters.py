
def filter_tools(
        queryset,
        category="",
        audience="",
        pricing=""
):
    if category:
        queryset = queryset.filter(
            categories__slug=category
        )
    if audience:
        queryset = queryset.filter(
            audiences__slug=audience
    )
    if pricing:
        queryset = queryset.filter(
            pricing_type=pricing
        )
    return queryset.distinct()