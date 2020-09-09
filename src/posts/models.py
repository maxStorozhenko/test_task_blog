from django.db import models
from django.utils import timezone


def photo_path(instance, filename):
    return f'{instance.id}/{filename}'


# У каждого поста должен быть автор, время публикации, время создания, время последнего обновления.
class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    author = models.CharField(max_length=50)
    published = models.BooleanField(default=False)
    pub_date = models.DateTimeField(null=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    picture = models.ImageField(upload_to=photo_path, blank=True, null=True)

    def save(self, *args, **kwargs):
        if self.published and self.pub_date is None:
            self.pub_date = timezone.now()
        elif not self.published and self.pub_date is not None:
            self.pub_date = None
        super().save(*args, **kwargs)
