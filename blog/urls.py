from django.urls import path
from .views import CategoryListWithBlogPostsAPIView,BlogListAPI,BlogDetailView

urlpatterns = [
    path('', CategoryListWithBlogPostsAPIView.as_view(), name='categories-with-blogposts'),
    path('latest/', BlogListAPI.as_view(), name='blogposts'),
    path('latest/<slug:slug>',BlogDetailView.as_view(),name='blogdetails')
]