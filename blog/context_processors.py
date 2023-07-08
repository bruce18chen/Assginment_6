from django.db.models import Count  # Add this line
from . import models
from .models import Topic


def base_context(request):
    top_topics = Topic.objects.annotate(post_count=Count('post')).order_by('-post_count')[:5]  # Update this line
    return {'top_topics': top_topics}
