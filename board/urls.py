from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostList.as_view(), name='postList'),
    path('insert/', views.PostInsert.as_view(), name='insertData'),
]