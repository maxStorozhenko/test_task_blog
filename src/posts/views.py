from django.views.generic import ListView, DetailView
from .models import Post


class PostsListView(ListView):
    queryset = Post.objects.filter(published=True).order_by('-pub_date')
    paginate_by = 10
    template_name = 'posts/posts-list.html'


class PostDetailView(DetailView):
    model = Post
    template_name = 'posts/post-detail.html'
