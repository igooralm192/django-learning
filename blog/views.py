from django.utils import timezone
from rest_framework import viewsets
from .serializers import PostSerializer
from .models import Post

# Create your views here.

class PostView(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
