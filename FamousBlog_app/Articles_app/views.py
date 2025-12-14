from django.shortcuts import render, get_object_or_404, redirect
from .models import Article

def article_list(request):
    articles = Article.objects.filter(status="published").order_by('-created_at')
    return render(request, 'articles/list.html', {"articles": articles})

def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    return render(request, 'articles/detail.html', {"article": article})

def article_create(request):
    if request.method == "POST":
        Article.objects.create(
            title=request.POST['title'],
            content=request.POST['content'],
            author=request.user,
            category_id=request.POST['category']
        )
        return redirect('article_list')
    return render(request, 'articles/create.html')

def article_delete(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.user == article.author or request.user.is_staff:
        article.delete()
    return redirect('article_list')

