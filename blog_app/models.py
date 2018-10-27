from django.db import models
from accounts.models import UserManager


class Blog(models.Model):
    class Meta:
        db_table = 'blog'

    user = models.ForeignKey(UserManager, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.user)


class Post(models.Model):
    class Meta:
        db_table = 'Post'

    blog = models.OneToOneField(
        Blog,
        on_delete=models.PROTECT,
    )
    title = models.CharField(max_length=100)
    image = models.ImageField(
        upload_to='media/',
        blank=True,
    )
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.blog) + '|' + str(self.title)


