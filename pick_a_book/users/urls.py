from django.urls import path
from .views import *

app_name = 'users'

from . import view_user

urlpatterns = [
    path('login/' , login_view , name="login_view"),
    path('register/' , register_view , name="register_view"),
    path('logout-view/' , logout_view , name="logout_view"),

    # path('verify/<token>/' , verify , name="verify"),
    # path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post_update'),
]
