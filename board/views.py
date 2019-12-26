from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, FormView, DetailView, UpdateView
from .models import Post
from django.contrib.auth.models import User
from django.utils import timezone
from .form import PostForm, CommentForm
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404

# Create your views here.

class PostList(ListView):
  template_name = 'board/post_list.html'
  context_object_name = 'post_list'
  model = Post

  def get_queryset(self):
    return Post.objects.filter(published_date__lte=timezone.now()).order_by('-id')


class PostInsert(CreateView):
  template_name = 'board/post_create.html'
  success_url = reverse_lazy('post_list')
  form_class = PostForm
  model = Post

  def form_valid(self, form):
    self.object = form.save(commit=False)
    self.object.author = User.objects.get(username='admin')
    self.object.save()
    print(self.object)
    return super().form_valid(form)


class PostDetail(DetailView):
  template_name = 'board/post_detail.html'
  context_object_name = 'post_detail'
  model = Post


class PostEdit(UpdateView):
  template_name = 'board/post_edit.html'
  context_object_name = 'post_edit'
  success_url = reverse_lazy('post_list')
  form_class = PostForm
  model = Post

def add_comment_to_post(request, pk):
  post = get_object_or_404(Post, pk=pk)
  if request.method == "POST":
    form = CommentForm(request.POST)
    if form.is_valid():
      comment = form.save(commit=False)
      comment.post = post
      comment.save()
      return redirect('post_detail', pk=post.pk)
  else:
    form = CommentForm()
  return render(request, 'board/add_comment_to_post.html', {'form': form})