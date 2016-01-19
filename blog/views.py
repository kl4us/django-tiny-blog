from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from django.core.paginator import Paginator
from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger

from .models import Post

class PostDetailView(DetailView):

    model = Post

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        return context

    def get_queryset(self):
        qs = super(PostDetailView, self).get_queryset()
        return qs.filter(approved=True)

class PostListView(ListView):

    model = Post
    paginate_by = 6

    def get_context_data(self, **kwargs):
        context = super(PostListView, self).get_context_data(**kwargs)
        post_list = Post.objects.filter(approved=True)
        paginator = Paginator(post_list, self.paginate_by)

        page = self.request.GET.get('page')

        try:
            object_list = paginator.page(page)
        except PageNotAnInteger:
            object_list = paginator.page(1)
        except EmptyPage:
            object_list = paginator.page(paginator.num_pages)

        context['object_list'] = object_list

        return context