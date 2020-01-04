from django.urls import path
from . import views 
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView,UserPostListView

urlpatterns = [
    path('', PostListView.as_view(), name = 'blog-home'),
    path('user/<str:username>', UserPostListView.as_view(), name = 'user-posts'),
    path('detail/<pk>/',PostDetailView.as_view(), name = 'post-detail'),
    path('post/new/',PostCreateView.as_view(),name = 'post-create'),
    path('detail/<pk>/update/',PostUpdateView.as_view(), name = 'post-update'),
    path('detail/<pk>/delete/',PostDeleteView.as_view(), name = 'post-delete'),
    path('about/', views.about, name = 'blog-about'),
]
