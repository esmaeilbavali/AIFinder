
from django.db import transaction
from django.core.exceptions import ValidationError

from .models import AITool


@transaction.atomic
def create_ai_tool(tool_data, categories=None, audiences=None):

    tool_data = tool_data.copy()

    name = tool_data.get("name", "")

    if not isinstance(name, str) or not name.strip():
        raise ValidationError("Tool name cannot be empty.")

    name = name.strip()

    if AITool.objects.filter(name__iexact=name).exists():
        raise ValidationError(
            "An AI tool with this name already exists."
        )

    tool_data["name"] = name

    tool = AITool.objects.create(**tool_data)

    if categories is not None:
        tool.categories.set(categories)

    if audiences is not None:
        tool.audiences.set(audiences)

    return tool


@transaction.atomic
def update_ai_tool(
    tool,
    tool_data=None,
    categories=None,
    audiences=None
):
    tool_data = (tool_data or {}).copy()

    if "name" in tool_data:

        name = tool_data["name"]

        if not isinstance(name, str) or not name.strip():
            raise ValidationError(
                "Tool name cannot be empty."
            )

        name = name.strip()

        if AITool.objects.filter(
            name__iexact=name
        ).exclude(
            pk=tool.pk
        ).exists():
            raise ValidationError(
                "An AI tool with this name already exists."
            )

        tool_data["name"] = name

    for field, value in tool_data.items():
        setattr(tool, field, value)

    if tool_data:
        tool.save()

    if categories is not None:
        tool.categories.set(categories)

    if audiences is not None:
        tool.audiences.set(audiences)

    return tool


@transaction.atomic
def set_tool_active_status(tool, is_active):

    tool.is_active = is_active

    tool.save(
        update_fields=["is_active", "updated_at"]
    )

    return tool
