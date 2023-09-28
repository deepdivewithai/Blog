from django.urls import path
from . import views

urlpatterns = [
    path('post/', views.PostListView.as_view()),
    path('', views.UserListView.as_view()),
    path('detail/<int:pk>', views.PostDetailView.as_view())
]