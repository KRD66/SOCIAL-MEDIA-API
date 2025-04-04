from django.urls import path
from .views import PostListCreateView, PostDetailView, CommentListCreateView, CommentDetailView,RegisterView,LoginView, LikePostView, FollowUnfollowView
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
     # Posts CRUD
    path('posts/', PostListCreateView.as_view(), name='post-list-create'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post-detail'),

# Comments CRUD (linked to a post)
    path('posts/<int:post_id>/comments/', CommentListCreateView.as_view(), name='comment-list-create'),
    path('comments/<int:pk>/', CommentDetailView.as_view(), name='comment-detail'),

    path('auth/register/', RegisterView.as_view(), name='register'),
    path('auth/login/', LoginView.as_view(), name='login'),
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('posts/<int:pk>/like/', LikePostView.as_view(), name='like-post'),
    path('users/<str:username>/follow/', FollowUnfollowView.as_view(), name='follow-user'),
]

