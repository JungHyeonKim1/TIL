from django.shortcuts import render, redirect
from .models import Article

# Create your views here.
def index(request):
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)

def new(request):
    return render(request, 'articles/new.html')

def create(request):
    # 폼에서 전달되는 data 를 받는 부분
    title = request.POST.get('title')
    content = request.POST.get('content')

    # DB에 저장.
    # 1 번 방법 (이디님이 가장 선호하시는 방법 !)
    # article = Article()
    # article.title = title
    # article.content = content
    # article.save()

    # # 2번 방법
    # article = Article(title=title, content=content)
    # article.save()

    # # 3번 방법 (왠만하면 리턴값을 받아주기 !)
    article = Article.objects.create(title=title, content=content)

    # return redirect 사용해서 index 경로로 요청을 보낼 거임.   임포트도 해주기~!~!~!
    return redirect('articles:detail', article.id)   # 이 형태는 별명의 문자열입니다.
    # redirect는 함수이고 파이썬이라서 콤마가 따로 더 붙지 않는 것이다?

def detail(request, id):
    # variable routing 사용하기!
    article = Article.objects.get(pk=id)
    context = {
        'article': article,
    }
    return render(request, 'articles/detail.html', context)

def edit(request, id):
    article = Article.objects.get(pk=id)
    context = {
        'article': article,
    }
    return render(request, 'articles/edit.html', context)

def update(request, id):
    # 수정하려는 데이터를 디비로부터 가져온다.
    article = Article.objects.get(pk=id)
    # 입력 받은 데이터로 수정
    article.title = request.POST.get('title')
    article.content = request.POST.get('content')
    # 저장
    article.save()

    return redirect('articles:detail', article.id)

def delete(request, id):
    # 삭제하려는 값을 디비로부터 가져온다.
    article = Article.objects.get(pk=id)
    article.delete()

    return redirect('articles:index')