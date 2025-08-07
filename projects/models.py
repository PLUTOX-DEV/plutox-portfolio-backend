
from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/')
    live_url = models.URLField(max_length=300, blank=True, null=True)  # ✅ snake_case
    github_url = models.URLField(max_length=300, blank=True, null=True)
    icon_names = models.JSONField(default=list)  # store list of icon names as strings

    def __str__(self):
        return self.title
