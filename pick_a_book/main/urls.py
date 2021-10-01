from django.urls import path
from .import views

app_name = 'main'

urlpatterns = [
    path('about/', views.about, name='about'),
    path('', views.home, name='home'),
    path('faq/', views.faq, name='faq'),
    path('confirm/admin/', views.adminConfirm, name='adminConfirm'),
]