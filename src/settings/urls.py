from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from posts.views import PostsListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', PostsListView.as_view(), name='list'),
    path('posts/', include('posts.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
