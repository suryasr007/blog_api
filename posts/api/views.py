from django.db.models import Q
from rest_framework import generics, mixins
from posts.models import BlogPost
from .serializer import BlogPostSerializer

# Create your views here.

class BlogPostAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    lookup_field = 'id'
    serializer_class = BlogPostSerializer


    def get_queryset(self):
        qs = BlogPost.objects.all()
        query = self.request.GET.get('q')
        if query is not None:
            qs = qs.filter(Q(title__icontains=query)|Q(content__icontains=query)).distinct()
        return qs

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
    def get_serializer_context(self, *args, **kwargs):
        return {"request": self.request}

class BlogPostRudView(generics.RetrieveUpdateDestroyAPIView):
    
    lookup_field = 'id'
    serializer_class = BlogPostSerializer

    def get_serializer_context(self, *args, **kwargs):
        return {"request": self.request}
    
    def get_queryset(self):
        return BlogPost.objects.all()