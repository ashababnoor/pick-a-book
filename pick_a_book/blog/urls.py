from django.urls import path
from .import views

app_name = 'blog'

from .views import *

urlpatterns = [
    path('' , home , name="home"),
    # path('comment-detail/<slug>', comment_detail, name="comment_detail"),
    path('add-blog/' , add_blog, name="add_blog"),
    path('blog-detail/<slug>' , blog_detail , name="blog_detail"),
    path('see-blog/' , see_blog , name="see_blog"),
    path('blog-delete/<id>' , blog_delete , name="blog_delete"),
    path('blog-update/<slug>/<id>' , blog_update , name="blog_update"),
    # path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post_update'),
]
