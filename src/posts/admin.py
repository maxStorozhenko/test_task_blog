from django.contrib import admin
from django.utils import timezone

from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'get_description', 'author', 'creation_date', 'updated_at', 'pub_date', 'picture')
    fields = ('title', 'body', 'author', 'picture', 'published')

    def get_description(self, obj):
        if len(obj.body) > 50:
            return obj.body[:50] + '...'
        else:
            return obj.body

    get_description.short_description = 'description'

    def save_model(self, request, obj, form, change):
        if obj.published and 'published' in form.changed_data:
            obj.pub_date = timezone.now()

        super().save_model(request, obj, form, change)


admin.site.register(Post, PostAdmin)
