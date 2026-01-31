from django.contrib import admin
from .models import Category, Project, ProjectImage, SiteSettings


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "created_at")
    prepopulated_fields = {"slug": ("name",)}


class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 1
    ordering = ("order",)


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "is_featured", "is_published", "created_at")
    list_filter = ("category", "is_featured", "is_published")
    list_editable = ("is_featured", "is_published")
    search_fields = ("title", "short_description")
    prepopulated_fields = {"slug": ("title",)}
    inlines = [ProjectImageInline]

    def cover_preview(self, obj):
        if obj.cover_image:
            return format_html('<img src="{}" width="100"/>', obj.cover_image.url)
        return "-"


@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):

    def has_add_permission(self, request):
        return not SiteSettings.objects.exists()

admin.site.register(Category)
admin.site.register(ProjectImage)
admin.site.register(SiteSettings)