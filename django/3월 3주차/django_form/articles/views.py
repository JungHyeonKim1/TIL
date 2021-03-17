from django.shortcuts import render, redirect

from .models import Article
from .forms import ArticleForm


def index(request):
    articles = Article.objects.all()

    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)


# def new(request):
#     form = ArticleForm()

#     context = {
#         'form': form,
#     }
#     return render(request, 'articles/new.html', context)


# def create(request):
#     # 값을 받아서 폼 인스턴스 생성.
#     form = ArticleForm(request.POST)
    
#     # 유효성 검사
#     if form.is_valid():
#         # DB에 저장 (ModelForm 으로 작성했을 때)
#         article = form.save() # return 은 저장된 data의 인스턴스
#         return redirect('articles:index')
    
#     context = {
#         'form': form,
#     }

#     return render(request, 'articles/new.html', context)


def create(request):
    if request.method == "POST":
        # def create : DB에 저장
        form = ArticleForm(request.POST)

        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', article.pk)

    else:
        # def new 동작 : page 를 보여주는 
        form = ArticleForm()

    context = {
        'form': form,
    }
    return render(request, 'articles/new.html', context)


def detail(request, pk):
    article = Article.objects.get(id=pk)
    context = {
        'article': article,
    }
    return render(request, 'articles/detail.html', context)


def edit(request, pk):
    article = Article.objects.get(id=pk)

    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', article.pk)

    else:
        form = ArticleForm(instance=article)

    context = {
        'form': form,
        'article': article,
    }
    return render(request, 'articles/edit.html', context)


def delete(request, pk):
    article = Article.objects.get(id=pk)
    if request.method == 'POST':
        article.delete()
        return redirect('articles:index')
    
    return redirect('articles:detail', article.pk)