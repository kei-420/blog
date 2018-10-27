from django.db import models


class Blog(models.Model):
    class Meta:
        db_table = 'blog'

    blog_name = models.CharField(
        max_length=255,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.blog_name)


class Comment(models.Model):
    class Meta:
        db_table = 'comment'

    title = models.CharField(
        max_length=255,
        blank=True,
    )
    text = models.TextField(
        blank=True,
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.text)
