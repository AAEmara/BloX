from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .models import Comment
from .serializers import CommentSerializer

class PostCommentsAPIView(generics.ListCreateAPIView):
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        return Comment.objects.filter(post_id=self.kwargs['pk']).order_by('created_at')

    def create(self, request, *args, **kwargs):
        post_id = self.kwargs['pk']
        data = request.data.copy()

        # Defaults if not provided
        data.setdefault('post', post_id)
        data.setdefault('user', request.user.id)

        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)

        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def perform_create(self, serializer):
        serializer.save()