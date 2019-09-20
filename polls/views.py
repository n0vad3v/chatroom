from django.shortcuts import render
from django.http      import HttpResponse,Http404
from django.template  import loader
from .models import Post,Comment
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import logout

# Create your views here.

def get_all_posts():
    all_posts = Post.objects.all().order_by('-post_created_at')
    all_dashboard_list = []
    for post in all_posts:
        each_post_with_comment = get_all_comments_for_post(post.post_title)
        all_dashboard_list.append(each_post_with_comment)
    return all_dashboard_list

def get_all_comments_for_post(title):
    post_object = Post.objects.get(post_title = title)
    comment_list = Comment.objects.filter(comment_on = title)
    print("What's the pinglun for"+title)
    print(comment_list)
    res = {}
    res['post_title'] = post_object.post_title
    res['post_content'] = post_object.post_content
    res['post_created_at'] = post_object.post_created_at
    res['post_created_by'] = post_object.post_created_by
    res['post_comment'] = comment_list
    return res

def login_page(request):
    if request.method == "GET":
        return render(request, 'login.html')
    if request.method == "POST":
        name = request.POST.get('name')
        password = request.POST.get('password')
        user = authenticate(request,username=name,password=password)
        if user is not None:
            login(request,user)
            return redirect('/dashboard')
        else:
            messages.warning(request, 'Wrong PWD~')
            return redirect('/login')

def register_page(request):
    if request.method == "GET":
        return render(request, 'register.html')
    if request.method =="POST":
        name = request.POST.get('name')
        password = request.POST.get('password')
        user = User.objects.create_user(username=name,password=password)
        messages.success(request, '你已经成功注册，开始登陆吧~')
        return redirect('/login')

def chat_page(request):
    all_posts = get_all_posts()
    res = {}
    res['all_posts'] = all_posts
    return render(request, 'chat.html',res)

def edit_page(request):
    return render(request,'edit.html')


def dashboard_page(request):
    username = request.user.username
    post_count = Post.objects.filter(post_created_by = username).count()
    # Begin created by Nova Kwok
    post_list = Post.objects.filter(post_created_by = username)
    # End created by Nova Kwok
    res = {}
    res['post_count'] = post_count
    res['post_list'] = post_list
    return render(request,'dashboard.html',res)

def create_post(request):
    username = request.user.username
    post_title = request.POST.get('post_title')
    post_title = post_title.replace(' ','-')
    post_content = request.POST.get('post_content')
    post = Post()
    post.post_title = post_title
    post.post_content = post_content
    post.post_created_by = username
    post.save()
    return redirect('/')

def delete_post(request,id):
    post_object = Post.objects.get(pk=id)
    post_object.delete()
    return redirect('/dashboard')

def post_comment(request):
    username = request.user.username
    post_title = request.POST.get('post_title')
    comment_content = request.POST.get('comment_content')
    comment = Comment()
    comment.comment_content = comment_content
    comment.comment_by = username
    comment.comment_on = post_title
    comment.save()
    return redirect('/')

def log_out(request):
    logout(request)
    return redirect('/login')
