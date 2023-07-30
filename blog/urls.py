
from . import views
from django.urls import path
from .views import LikeCommentView, DislikeCommentView
from .views import PostDetailView, PostComment
from .views import UserLoginView

from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('posts/', views.PostListView.as_view(), name='posts'),
    path('contact/', views.contact, name='contact'),
    path('terms/', views.terms_and_conditions, name='terms-and-conditions'),
    path('topics/', views.TopicListView.as_view(), name='topic-list'),
    path('topics/<slug:slug>/', views.TopicDetailView.as_view(), name='topic-detail'),
    path('contest/', views.contest, name='contest'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('post/<int:pk>/comment/', PostComment.as_view(), name='post_comment'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('comments/<int:pk>/like', views.LikeCommentView.as_view(), name='like_comment'),
    path('comments/<int:pk>/dislike', views.DislikeCommentView.as_view(), name='dislike_comment'),
]

