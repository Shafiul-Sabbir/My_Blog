from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Post
from django.contrib.auth.models import User
from django.views.generic import (
    ListView, 
    DetailView, 
    CreateView,
    UpdateView,
    DeleteView
)
# Create your views here.
def home(request):
    context = {
        'posts' : Post.objects.all(),
        'title' : 'Home'
        }
    return render(request, 'blog/home.html', context)

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html' # <app> / <model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted'] # for ordering the newest blog to the top of the page.
    paginate_by = 4
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Blogs'
        return context
    
class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html' # <app> / <model>_<viewtype>.html
    context_object_name = 'posts'
    paginate_by = 4
    
    def get_queryset(self):
        user = get_object_or_404(User, username = self.kwargs.get('username'))
        return Post.objects.filter(author = user).order_by('-date_posted')
    
    """
    the upper function 'get_queryset' must be this spelling. if there occurs any mispelling 
    then the posts of every particular author will not be shown correctly at
    user_posts.html page. 
    """
    
class PostDetailView(DetailView):
    model = Post
    
class PostCreateView( LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView( LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']
    
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
    context = {
        'posts' : Post.objects.all(),
        'post_number' : Post.objects.all().count(),
        'author_number' : Post.objects.all().values('author').distinct().count(),
        'title' : 'About'
        }
    return render(request, 'blog/about.html', context)

def contact_us(request):
    context = {
        'title' : 'Contact Us'
        }
    return render(request, 'blog/contact_us.html', context)

def contact_us_success(request):
    name = request.POST['name']
    email = request.POST['email']
    message = request.POST['message']
    context = {
        'name' : name,
        'email' : email,
        'message' : message,
        'title' : 'Contact Us'
        }
    return render(request, 'blog/contact_us_success.html', context)


