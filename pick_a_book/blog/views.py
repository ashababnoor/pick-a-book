from os import name
from django.shortcuts import render , redirect
from django.urls.conf import path
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
# from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


from .models import BlogModel
from .comment_form import CommentForm
from django.shortcuts import render, get_object_or_404
# Create your views here.

from .form import *
from django.contrib.auth import logout 


def logout_view(request):
    logout(request)
    return redirect('/')


def home(request):
    context = {'blogs' : BlogModel.objects.all().order_by('-id')}
    return render(request , 'blog/home.html' , context)


def blog_detail(request , slug):
    # context = {}
    blog_obj = BlogModel.objects.filter(slug = slug).first()
    context = {'comments' : Comment.objects.filter(blog_id = slug).all()}
    print(context)
    context['blog_obj'] =  blog_obj
    try:
        if request.method == 'POST':
            # form = Comment(request.POST)
            # print(request.FILES)
            comment = request.POST.get('comment')
            user = request.user
            print(comment)
            print('my name comment')
            
            blog_obj1 = Comment.objects.create(
                blog_id = slug, name = user , body = comment
            )
            print(blog_obj1)
            # return redirect('/blog-detail/{{slug}}')     
    except Exception as e:
        print(e)
        
    print(context['comments'])
    return render(request , 'blog/blog_detail.html' , context)


def see_blog(request):
    context = {}
    
    try:
        blog_objs = BlogModel.objects.filter(user = request.user)
        context['blog_objs'] =  blog_objs
    except Exception as e: 
        print(e)
    
    print(context)
    return render(request , 'blog/see_blog.html' ,context)


def add_blog(request):
    context = {'form' : BlogForm}
    try:
        print("jubaer1")
        if request.method == 'POST':
            print("jubaer2")
            form = BlogForm(request.POST)
            print(request.FILES)
            image = request.FILES['image']
            title = request.POST.get('title')
            user = request.user
            
            if form.is_valid():
                content = form.cleaned_data['content']
            
            blog_obj = BlogModel.objects.create(
                user = user , title = title, 
                content = content, image = image
            )
            print(blog_obj)
            return redirect('blog/add-blog/')
            
    except Exception as e :
        print(e)
    print("jubaer3")
    return render(request , 'blog/add_blog.html' , context)
    

def blog_update(request , slug, id):
    context = {}
    try:

        blog_obj = BlogModel.objects.get(slug = slug)
       
        
        if blog_obj.user != request.user:
            return redirect('/')
        
        initial_dict = {'content': blog_obj.content}
        form = BlogForm(initial = initial_dict)
        if request.method == 'POST':
            form = BlogForm(request.POST)
            print(request.FILES)
            image = request.FILES['image']
            title = request.POST.get('title')
            user = request.user
            
            if form.is_valid():
                content = form.cleaned_data['content']
            
            blog_obj = BlogModel.objects.create(
                user = user , title = title, 
                content = content, image = image
            )
            
            blog_delete(request, id)
            print("jubaer1")
        
        context['blog_obj'] = blog_obj
        context['form'] = form
    except Exception as e :
        print(e)

    return render(request , 'blog/update_blog.html' , context)


def blog_delete(request , id):
    print("jubaer2")
    try:
        blog_obj = BlogModel.objects.get(id = id)
        
        if blog_obj.user == request.user:
            blog_obj.delete()
        
    except Exception as e :
        print(e)

    return redirect('blog/see-blog/')



