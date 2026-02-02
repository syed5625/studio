from django.contrib import admin
from django.utils.html import format_html
from .models import Category, Project, ProjectImage, SiteSettings
from .models import Inquiry

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "created_at")
    prepopulated_fields = {"slug": ("name",)}
    search_fields = ("name",)


class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 1
    ordering = ("order",)


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "category",
        "is_featured",
        "is_published",
        "created_at",
    )
    list_filter = ("category", "is_featured", "is_published")
    list_editable = ("is_featured", "is_published")
    search_fields = ("title", "short_description")
    prepopulated_fields = {"slug": ("title",)}
    inlines = [ProjectImageInline]
    ordering = ("-created_at",)


    def cover_preview(self, obj):
        if obj.cover_image:
            return format_html(
                '<img src="{}" width="80" style="border-radius:4px;" />',
                obj.cover_image.url,
            )
        return "-"

    cover_preview.short_description = "Cover"


@admin.register(ProjectImage)
class ProjectImageAdmin(admin.ModelAdmin):
    list_display = ("project", "order", "caption")
    list_filter = ("project",)
    ordering = ("project", "order")


@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return not SiteSettings.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False

@admin.register(Inquiry)
class InquiryAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "created_at")
    list_filter = ("created_at",)
    search_fields = ("name", "email", "message")
    readonly_fields = ("created_at",)