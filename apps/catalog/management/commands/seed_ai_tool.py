import random

from faker import Faker

from django.core.management.base import BaseCommand
from django.db import transaction
from django.db.models import JSONField

from apps.catalog.models import AITool
from apps.taxonomy.models import Category, Audience


fake = Faker()


class Command(BaseCommand):

    help = "Create fake AI tools for development and testing"

    TOOL_NAMES = [
        "NeuraWriter",
        "PixelMind",
        "CodePilot",
        "DataGenius",
        "VoiceCraft",
        "VisionAI",
        "SmartTutor",
        "PromptFlow",
        "ImageForge",
        "TextGenius",
        "DevAssistant",
        "VideoMagic",
        "AudioMind",
        "DesignBot",
        "ResearchMate",
        "LearnAI",
        "CodeSphere",
        "PhotoWizard",
        "ContentCraft",
        "ChatSphere",
        "TranslatePro",
        "MusicGenie",
        "ResumeAI",
        "MarketingMind",
        "StudyBuddy",
        "DocuSmart",
        "DataPilot",
        "ArtVision",
        "SpeechFlow",
        "TaskGenius",
    ]

    CATEGORIES = [
        ("Programming", "programming"),
        ("Image Generation", "image-generation"),
        ("Text Generation", "text-generation"),
    ]

    AUDIENCES = [
        ("Teachers", "teachers"),
        ("Developers", "developers"),
        ("Students", "students"),
    ]

    def add_arguments(self, parser):

        parser.add_argument(
            "--count",
            type=int,
            default=30,
            help="Number of AI tools to create"
        )

    def handle(self, *args, **options):

        count = options["count"]

        if count < 1:
            self.stdout.write(
                self.style.ERROR("Count must be greater than zero.")
            )
            return

        with transaction.atomic():

            categories = self.create_taxonomy(
                Category,
                self.CATEGORIES
            )

            audiences = self.create_taxonomy(
                Audience,
                self.AUDIENCES
            )

            created_count = 0

            for i in range(1, count + 1):

                name = self.TOOL_NAMES[
                    (i - 1) % len(self.TOOL_NAMES)
                ]

                if i > len(self.TOOL_NAMES):
                    name = f"{name} {i}"

                slug = self.make_slug(name)

                if AITool.objects.filter(slug=slug).exists():
                    continue

                tool = self.create_tool(name, slug)

                tool.categories.set(
                    random.sample(
                        categories,
                        k=random.randint(1, len(categories))
                    )
                )

                tool.audiences.set(
                    random.sample(
                        audiences,
                        k=random.randint(1, len(audiences))
                    )
                )

                created_count += 1

                self.stdout.write(
                    self.style.SUCCESS(f"Created: {name}")
                )

        self.stdout.write(
            self.style.SUCCESS(
                f"\nSuccessfully created {created_count} AI tools."
            )
        )

    def create_taxonomy(self, model, items):

        objects = []

        for name, slug in items:

            obj, created = model.objects.get_or_create(
                slug=slug,
                defaults={"name": name}
            )

            objects.append(obj)

        return objects

    def make_slug(self, name):

        from django.utils.text import slugify

        return slugify(name)

    def create_tool(self, name, slug):

        pricing_choices = [
            choice[0]
            for choice in AITool._meta.get_field(
                "pricing_type"
            ).choices
        ]

        pricing_type = random.choice(pricing_choices)

        tool_data = {
            "name": name,
            "slug": slug,
            "description": fake.paragraph(nb_sentences=4),
            "website_url": f"https://{slug}.example",
            "pricing_type": pricing_type,
            "price_details": fake.sentence(),
            "is_active": True,
        }

        # Support both TextField and JSONField
        for field_name in ["features", "pros", "cons"]:

            field = AITool._meta.get_field(field_name)

            if isinstance(field, JSONField):

                tool_data[field_name] = [
                    fake.sentence()
                    for _ in range(3)
                ]

            else:

                tool_data[field_name] = "\n".join([
                    fake.sentence()
                    for _ in range(3)
                ])

        return AITool.objects.create(**tool_data)