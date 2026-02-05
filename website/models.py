from django.db import models
from django.utils.text import slugify
from cloudinary.models import CloudinaryField
from django.core.exceptions import ValidationError


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(unique=True, blank=True)
    description = models.TextField(blank=True)

    image = CloudinaryField(
        "Category Image",
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["name"]

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name




class Project(models.Model):
    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        related_name="projects"
    )

    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)

    short_description = models.CharField(max_length=300)
    description = models.TextField(blank=True)

    cover_image = CloudinaryField(
        "Project Cover",
        blank=True,
        null=True
    )

    is_featured = models.BooleanField(default=False)
    is_published = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.title)
            slug = base_slug
            counter = 1
            while Project.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title



class ProjectImage(models.Model):
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name="images"
    )

    image = CloudinaryField(
        "Project Image",
        blank=True,
        null=True
    )

    caption = models.CharField(max_length=200, blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return f"{self.project.title} – Image {self.order}"



class SiteSettings(models.Model):
    hero_title = models.CharField(max_length=200)
    hero_subtitle = models.CharField(max_length=300)

    hero_image = CloudinaryField(
        "Hero Image",
        blank=True,
        null=True
    )

    footer_text = models.CharField(max_length=200)
    contact_email = models.EmailField()

    instagram_url = models.URLField(blank=True)
    facebook_url = models.URLField(blank=True)

    class Meta:
        verbose_name_plural = "Site Settings"

    def __str__(self):
        return "Site Settings"



class Inquiry(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"Inquiry from {self.name}"


def validate_image_size(image):
    max_size = 5 * 1024 * 1024
    if image and image.size > max_size:
        raise ValidationError("Image file too large (max 5MB).")