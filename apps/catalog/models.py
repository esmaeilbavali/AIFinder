from django.db import models
from apps.taxonomy.models import Category, Audience

# Create your models here.


class AITool(models.Model):

    PRICING_CHOICES = [
        ("free", "Free"),
        ("freemium", "Freemium"),
        ("paid", "Paid"),
        ("custom", "Custom Pricing"),
    ]

    name = models.CharField(max_length=150)

    slug = models.SlugField(unique=True)

    description = models.TextField()

    website_url = models.URLField()

    pricing_type = models.CharField(
        max_length=20,
        choices=PRICING_CHOICES,
        default="freemium"
    )

    price_details = models.TextField(blank=True)

    features = models.TextField(blank=True)

    pros = models.TextField(blank=True)

    cons = models.TextField(blank=True)

    categories = models.ManyToManyField(
        Category,
        related_name="tools"
    )

    audiences = models.ManyToManyField(
        Audience,
        related_name="tools"
    )
    image = models.ImageField(
    upload_to="ai_tools/",
    blank=True,
    null=True
)

    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name