from django.urls import path
from .views import CategoryWithBlogPostsView

urlpatterns = [
    path('', CategoryWithBlogPostsView.as_view(), name='categories-with-blogposts'),
]