
from users.admin import CustomUserAdmin
from django.shortcuts import render, get_object_or_404
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Post, Comment, Reply
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from users.models import CustomUser
from django.views import generic
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'situmon/home.html', context)


class PublicPostListView(ListView):
    model = Post
    template_name = 'situmon/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-id']
    paginate_by = 10


class UserPostListView(ListView):
    model = Post
    template_name = 'situmon/user_posts.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    paginate_by = 10

    def get_queryset(self):
        user = get_object_or_404(CustomUser, username=self.kwargs.get('username'), )
        return Post.objects.filter(author=user).order_by('-id')


class PostDetailView(DetailView):
    model = Post

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'description','text']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'text']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

def about(request):
    return render(request, 'situmon/about.html', {'title': 'About'})


class CommentView(generic.CreateView):
    """/comment/post_pk コメント投稿."""
    model = Comment
    fields = ('text',)
    template_name = 'situmon/comment_form.html'
 
    def form_valid(self, form):
        post_pk = self.kwargs['pk']
        post = get_object_or_404(Post, pk=post_pk)
 
        # 紐づく記事を設定する
        comment = form.save(commit=False)
        comment.target = post
        comment.name = self.request.user
        comment.save()
 
        # 記事詳細にリダイレクト
        return redirect('situmon:post-detail', pk=post_pk)
 
class ReplyView(generic.CreateView):
    """/reply/comment_pk 返信コメント投稿."""
    model = Reply
    fields = ('text',)
    template_name = 'situmon/comment_form.html'
 
    def form_valid(self, form):
        comment_pk = self.kwargs['pk']
        comment = get_object_or_404(Comment, pk=comment_pk)
 
        # 紐づくコメントを設定する
        reply = form.save(commit=False)
        reply.target = comment
        reply.name = self.request.user
        reply.save()
 
        # 記事詳細にリダイレクト
        return redirect('situmon:post-detail', pk=comment.target.pk)