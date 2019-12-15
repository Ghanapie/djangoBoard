from django.shortcuts import render
from django.views.generic import ListView, CreateView, FormView
from .models import Post
from django.contrib.auth.models import User
from django.utils import timezone
from .form import PostForm
from django.urls import reverse_lazy
# Create your views here.

class PostList(ListView):
    template_name = 'board/postList.html'
    context_object_name = 'postList'
    model = Post

    def get_queryset(self):
        return Post.objects.filter(published_date__lte=timezone.now()).order_by('-id')


class PostInsert(CreateView):
    template_name = 'board/insertData.html'
    success_url = reverse_lazy('postList')
    form_class = PostForm
    model = Post

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            print("aaa")
            return self.form_invalid(form)


    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = User.objects.get(username='admin')
        self.object.save()
        print(self.object)
        return super().form_valid(form)