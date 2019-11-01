from django.db import models

# Create your models here.

class Resource(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField(max_length=200)
    link = models.URLField(max_length=200)

    def __str__(self):
        return self.title

class Video(Resource):
    def __str__(self):
        return self.title

class Document(Resource):
    def __str__(self):
        return self.title

class Website(Resource):
    def __str__(self):
        return self.title

# Page base model
class Page(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=256, blank=True)

    def __str__(self):
        return self.title

# Homepage model - potential double entry & creation problem
class Homepage(Page):
    instruction_title = models.CharField(max_length=100)
    instruction_text = models.CharField(max_length=200)

    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural = "Home page"

# Resources page
class ResourcesPage(Page):
    banner_image = models.URLField(max_length=200)
    animated_gif = models.URLField(max_length=200)

    def __str__(self):
        return self.title

# Reusable Resource Module - "child of Page, Many-to-one (FK)"
class ResourceModule(models.Model):
    title = models.CharField(max_length=64)
    description = models.TextField(max_length=256)
    page = models.ForeignKey('Page', on_delete=models.PROTECT)

    PRIORITY_CHOICES = (
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
        (6, 6),
        (7, 7),
        (8, 8),
        (9, 9),
        (10, 10)
    )

    priority = models.IntegerField(choices=PRIORITY_CHOICES, default=5, help_text='Use this field to determine relative position of this module on the page. Lower numbers appear earlier on page.')
    resources = models.ManyToManyField(Resource)

    def __str__(self):
        return self.title

# Design Assets model
class DesignAssets(models.Model):
    video_img = models.URLField(max_length=200)
    website_img = models.URLField(max_length=200)
    document_img = models.URLField(max_length=200)

    def __str__(self):
        return 'Design Assets'
    class Meta:
        verbose_name_plural = "Design assets"

# Global Settings
class GlobalSettings(models.Model):
    contact = models.EmailField(max_length=70)

    def __str__(self):
        return 'Global Settings'
    class Meta:
        verbose_name_plural = "Global settings"
