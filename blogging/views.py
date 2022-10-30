from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from blogging.models import Post


class BlogDetailView(DetailView):
    # DetailView.get_object() will only try and find a Post matching pk if it's
    # in the set of Posts that have been published
    queryset = Post.objects.exclude(published_date__exact=None)
    template_name = "blogging/detail.html"


class BlogListView(ListView):
    # Only show posts that have been published, and display them in reverse
    # chronological order
    queryset = Post.objects.exclude(published_date__exact=None).order_by(
        "-published_date"
    )
    template_name = "blogging/list.html"
