# views.py

from django.shortcuts import render, get_object_or_404, reverse
from django.views.generic import ListView, DetailView, FormView, View, TemplateView
from django.views.generic.detail import SingleObjectMixin
from .models import Post, Comment, Topic
from .forms import CommentForm, ContestEntryForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.http import JsonResponse
from django.db.models import F

class LikeCommentView(LoginRequiredMixin, View):
    def post(self, *args, **kwargs):
        comment = get_object_or_404(Comment, id=self.kwargs.get('pk'))
        comment.likes = F('likes') + 1
        if comment.dislikes > 0:
            comment.dislikes = F('dislikes') - 1
        comment.save()
        comment.refresh_from_db()
        return JsonResponse({'likes': comment.likes, 'dislikes': comment.dislikes})

class DislikeCommentView(LoginRequiredMixin, View):
    def post(self, *args, **kwargs):
        comment = get_object_or_404(Comment, id=self.kwargs.get('pk'))
        comment.dislikes = F('dislikes') + 1
        if comment.likes > 0:
            comment.likes = F('likes') - 1
        comment.save()
        comment.refresh_from_db()
        return JsonResponse({'dislikes': comment.dislikes, 'likes': comment.likes})







class UserLoginView(LoginView):
    template_name = 'login.html'



class PostComment(LoginRequiredMixin, SingleObjectMixin, FormView):
    model = Post
    form_class = CommentForm
    template_name = 'post_detail.html'

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)

    def get_form_kwargs(self):
        kwargs = super(PostComment, self).get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs

    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.post = self.object
        comment.user = self.request.user  # Add this line to set the comment's user
        comment.save()
        return super().form_valid(form)

    def get_success_url(self):
        post = self.get_object()
        return reverse('post_detail', kwargs={'pk': post.pk}) + '#comments'


class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'  # Update this to your post detail template
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = Comment.objects.filter(post=self.object)
        context['comment_form'] = CommentForm()  # Add this line
        return context


def contest(request):
    if request.method == 'POST':
        form = ContestEntryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = ContestEntryForm()
    return render(request, 'contest.html', {'form': form})


class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        latest_posts = Post.objects.published().order_by('-published_date')[:3]
        context['latest_posts'] = latest_posts
        return context


class PostListView(ListView):
    model = Post
    template_name = 'posts.html'
    context_object_name = 'posts'
    paginate_by = 10


class AboutView(TemplateView):
    template_name = 'about.html'


class TopicListView(ListView):
    model = Topic
    template_name = 'topic_list.html'
    context_object_name = 'topics'


class TopicDetailView(DetailView):
    model = Topic
    template_name = 'topic_detail.html'
    context_object_name = 'topic'


def terms_and_conditions(request):
    return render(request, 'terms_and_conditions.html')


def contact(request):
    return render(request, 'contact.html')







