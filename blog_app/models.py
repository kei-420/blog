from django.db import models


class Blog(models.Model):
    blog_name = models.CharField(
        max_length=255,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.blog_name


class Comment(models.Model):
    title = models.CharField(
        max_length=255,
        blank=True,
    )
    text = models.TextField(
        blank=True,
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text
