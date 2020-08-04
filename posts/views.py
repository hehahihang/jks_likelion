from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from django.contrib.auth import get_user_model



def new(request):
    return render(request, 'posts/new.html')

def create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        image = request.FILES.get('image')
        user = request.user
        Post.objects.create(title = title, content=content, image=image, user=user)
    return redirect('posts:main') 

def main(request):
    posts = Post.objects.all().order_by("-created_at")
    return render(request, 'posts/main.html', {'posts' : posts})

def show(request, id):
    post = Post.objects.get(pk=id)
    post.view_count += 1
    post.save()
    return render(request, 'posts/show.html', {'post' : post})

def update(request, id):
    post = get_object_or_404(Post, pk=id)
    if request.method == "POST":
        post.title = request.POST['title']
        post.content = request.POST['content']
        post.image = request.FILES.get('image')
        post.save()
        return redirect('posts:show', post.id) 
        #post.id 값을 가지고 posts앱의 show라는 이름의 url을 거쳐서 view의 def show를 실행
    return render(request, 'posts/update.html', {"post":post}) 
    #POST방식이 아닌 경우에는 해당 post를 직접가져가서 update.html을 띄워준다.

def delete(request, id):
    post = get_object_or_404(Post, pk=id)
    post.delete()
    return redirect('posts:main')

def like(request, id):
    post = get_object_or_404(Post, pk=id)
    #좋아요 취소
    if request.user in post.like_users.all():
        post.like_users.remove(request.user)
    else:
        post.like_users.add(request.user)

    return redirect('posts:main')
    ##다시 돌아가서 show.html을 보여주고싶은데 어떻게해야되는지 궁금쓰