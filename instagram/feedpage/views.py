from django.shortcuts import render, redirect
from feedpage.models import Feed, FeedComment, Like

def index(request):
    if request.method == 'GET':
        feeds = Feed.objects.all()
        return render(request, 'feedpage/index.html', {'feeds': feeds})
        #feeds:feeds는 dict 타입 {'html변수': view변수}
        #dict 타입 표시 잘해주기
    
    elif request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        photo =  request.FILES.get('photo', False)
        Feed.objects.create(title=title, content=content, author=request.user, photo=photo)
        return redirect('/feeds')
        #redirect는 다시 원래 페이지로 갈때만 쓰겠군 url 갔다가 다시 왔다가 GET으로 가서 render 할테니

def new(request):
    return render(request, 'feedpage/new.html')

def show(request, id):
    feed = Feed.objects.get(id=id) 
    #id를 받아서 그 id를 가진 Feed.objects를 찾고 feed라 명명
    return render(request, 'feedpage/show.html', {'feed':feed})
    #views.py 의 feed 데이터를 show.html의 'feed'로 보냄

def delete(request, id):
    feed = Feed.objects.get(id=id)
    feed.delete()
    return redirect('/feeds')

def edit(request, id):
    if request.method == "GET":
        feed = Feed.objects.get(id=id)
        return render(request, 'feedpage/edit.html', {'feed':feed})
    elif request.method == "POST":
        feed = Feed.objects.get(id=id)
        if request.POST['title'] is not None:
            feed.title = request.POST['title']
        if request.POST['content'] is not None:
            feed.content = request.POST['content']
        feed.save()
        return redirect('/feeds')

def create_comment(request, id):
    content = request.POST['content']
    FeedComment.objects.create(feed_id=id, content=content, author=request.user)
    return redirect('/feeds')

def delete_comment(request, id, cid):
    c = FeedComment.objects.get(id=cid)
    c.delete()
    return redirect('/feeds')

def feed_like(request, pk):
    feed = Feed.objects.get(id = pk)
    like_list = feed.like_set.filter(user_id = request.user.id)
    if like_list.count() > 0:
        feed.like_set.get(user_id = request.user.id).delete()
    else:
        Like.objects.create(user_id = request.user.id, feed_id = feed.id)
    return redirect ('/feeds') 

