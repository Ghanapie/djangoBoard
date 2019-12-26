from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostList.as_view(), name='post_list'),
    path('create/', views.PostInsert.as_view(), name='post_create'),
    path('detail/<int:pk>/', views.PostDetail.as_view(), name='post_detail'),
    path('edit/<int:pk>/', views.PostEdit.as_view(), name='post_edit'),
    path('detail/<int:pk>/comment/', views.add_comment_to_post, name='add_comment_to_post'),
]