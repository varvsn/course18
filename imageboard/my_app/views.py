from django.shortcuts import render, get_object_or_404, redirect
#from django.template import RequestContext
from django.contrib import messages

from my_app.forms import New_Post_Form, New_Comment_Form
from my_app.models import Post, Comment

def index(request):
    if request.method == 'GET':
        posts = Post.objects.order_by('created_date')
        form = New_Post_Form()
        return render(request, 'index.html', {'form': form, 'posts': posts})  #Путь до папки с темплейтами, у каждого апп он свой

    if request.method == 'POST':
        form = New_Post_Form(data=request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.title = form.cleaned_data['title']
            post.author = form.cleaned_data['author']
            post.post_body = form.cleaned_data['mess_txt']
            post.publish()
            messages.success(request, 'A very good Post number {} was added!'.format(post.id))
            return render(request, 'flash_page.html', {'form': form})
        else:
            messages.error(request, 'Error!')
        return render(request, 'flash_page.html', {'form': form})


def add_comment(request, post_id):
    if request.method == 'POST':
        form = New_Comment_Form(data=request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post_id = int(post_id)
            comment.author = form.cleaned_data['author']
            comment.comment_body = form.cleaned_data['comment_body']
            comment.publish()
            messages.success(request, 'A very good comment for Post number {} was added!'.format(post_id))
            return render(request, 'flash_page.html', {'form': form})
        else:
            messages.error(request, 'Error!')
        return render(request, 'flash_page.html', {'form': form})



    pass


def del_all(request):
    if request.method == 'GET':
        Post.objects.all().delete()
        messages.warning(request, 'All data deleted!')
        return render(request, 'flash_page.html')

