from django.shortcuts import render, get_object_or_404, redirect
from .models import Blog
from .models import Portfolio
from django.utils import timezone
from django.core.paginator import Paginator
from .form import BlogPost

# Create your views here.

def home(request):

    blogs = Blog.objects
    blog_list = Blog.objects.all()
    paginator = Paginator(blog_list,3)
    page = request.GET.get('pages')
    posts = paginator.get_page(page)
    return render(request,'home.html', {'blogs' : blogs, 'posts' : posts})

def new(request):

    return render(request, 'new.html')

def create(request):

    blog = Blog()
    blog.title = request.GET['title']
    blog.body = request.GET['body']
    blog.pub_date = timezone.datetime.now()
    blog.save()
    blogs = Blog.objects
    
    return render(request, 'home.html', {'blogs' : blogs})

    #return redirect('/')

def portfolio(request):
    return render(request, 'portfolio.html')

def detail(request, blog_id):

    blog_detail = get_object_or_404(blog, pk=blog_id)

    return render(request, 'detail.html', {'blog' : blog_detail})

def portfolio(request):
    portfolios=Portfolio.objects
    return render(request, 'portfolio.html', {'portfolios' : portfolios})

def blogpost(request):

    if request.method =='POST':
        form = BlogPost(request.POST)
        if form.is_valid():
            post = form.save(commit = False)
            post.pub_date = timezone.now()
            post.save()
            print('실행 오케이!')
            return redirect('home')

    else:

        form = BlogPost()
        print('실행 오케이!')
        return render(request, 'new.html', {'form' : form})