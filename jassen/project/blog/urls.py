from django.urls import path
from . import views
app_name = 'blog'
urlpatterns = [
    path('<int:pk>/', views.IndexView.as_view(), name='index'),
    path('post/<int:post_id>/', views.PostView.as_view(), name='post'),
]