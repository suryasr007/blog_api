from django.urls import path
from .views import BlogPostRudView, BlogPostAPIView

urlpatterns = [
    path('', BlogPostAPIView.as_view(), name='post_create'),    
    path('<int:id>/', BlogPostRudView.as_view(), name='post_rud')
]