# blog/views.py

from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from . import models
from django.shortcuts import render
from .models import Post

class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        latest_posts = models.Post.objects.published().order_by('-published_date')[:3]
        context['latest_posts'] = latest_posts
        return context

class PostListView(ListView):
    model = Post
    template_name = 'posts.html'  # your template name
    context_object_name = 'posts'
    paginate_by = 10


class AboutView(TemplateView):
    template_name = 'about.html'

class TopicListView(ListView):
    model = models.Topic
    template_name = 'topic_list.html'  # change this line
    context_object_name = 'topics'


class TopicDetailView(DetailView):
    model = models.Topic
    template_name = 'topic_detail.html'
    context_object_name = 'topic'

def terms_and_conditions(request):
   return render(request, 'terms_and_conditions.html')


def contact(request):
   return render(request, 'contact.html')
