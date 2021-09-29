
from django.urls import path
from .views import *
from . import view_user

urlpatterns = [
    path('' , home , name="home"),
    path('login/' , login_view , name="login_view"),
    path('register/' , register_view , name="register_view"),
    # path('comment-detail/<slug>', comment_detail, name="comment_detail"),
    path('add-blog/' , add_blog, name="add_blog"),
    path('blog-detail/<slug>' , blog_detail , name="blog_detail"),
    path('see-blog/' , see_blog , name="see_blog"),
    path('blog-delete/<id>' , blog_delete , name="blog_delete"),
    path('blog-update/<slug>/<id>' , blog_update , name="blog_update"),
    path('logout-view/' , logout_view , name="logout_view"),
    # path('verify/<token>/' , verify , name="verify"),
    # path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post_update'),
]
