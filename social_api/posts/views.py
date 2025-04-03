from rest_framework import generics,status
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate

class PostListCreateView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class CommentListCreateView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class CommentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

# Generate JWT Tokens for a user
def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

# User Registration View
class RegisterView(APIView):
    permission_classes = [AllowAny]  # Allow anyone to register

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        if not username or not password:
            return Response({'error': 'Username and password are required'}, status=status.HTTP_400_BAD_REQUEST)

        if User.objects.filter(username=username).exists():
            return Response({'error': 'Username already exists'}, status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.create_user(username=username, password=password)
        token = get_tokens_for_user(user)

        return Response({'message': 'User registered successfully', 'token': token}, status=status.HTTP_201_CREATED)

# User Login View
class LoginView(APIView):
    permission_classes = [AllowAny]  # Allow anyone to log in

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username=username, password=password)
        if user is None:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

        token = get_tokens_for_user(user)
        return Response({'message': 'Login successful', 'token': token}, status=status.HTTP_200_OK)


class LikePostView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]  # Only logged-in users can like/unlike

    def post(self, request, pk):
        post = Post.objects.get(pk=pk)
        user = request.user

        if user in post.likes.all():
            post.likes.remove(user)  # Unlike
            message = "Post unliked"
        else:
            post.likes.add(user)  # Like
            message = "Post liked"

        return Response({'message': message, 'likes_count': post.likes.count()}, status=status.HTTP_200_OK)
    
    
    
class FollowUnfollowView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, username):
        from .models import Profile  # Import inside the function to avoid circular import
        try:
            user_to_follow = User.objects.get(username=username)
        except User.DoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)

        if request.user == user_to_follow:
            return Response({"error": "You cannot follow yourself"}, status=status.HTTP_400_BAD_REQUEST)

        user_profile = request.user.profile
        target_profile = user_to_follow.profile

        if user_profile in target_profile.followers.all():
            target_profile.followers.remove(request.user)
            message = "Unfollowed successfully"
        else:
            target_profile.followers.add(request.user)
            message = "Followed successfully"

        return Response({"message": message, "followers_count": target_profile.followers.count()}, status=status.HTTP_200_OK)


