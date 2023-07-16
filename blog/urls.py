from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('posts/', views.PostListView.as_view(), name='posts'),
    path('contact/', views.contact, name='contact'),
    path('terms/', views.terms_and_conditions, name='terms-and-conditions'),
    path('topics/', views.TopicListView.as_view(), name='topic-list'),
    path('topics/<slug:slug>/', views.TopicDetailView.as_view(), name='topic-detail'),
    path('contest/', views.contest, name='contest'),
]
