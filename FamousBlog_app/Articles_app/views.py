from django.shortcuts import render, redirect, get_object_or_404
from .models import Article
from .forms import ArticleForm
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.db.models import Q

@login_required
def article_create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.save()
            return redirect('articles')
    else:
        form = ArticleForm()
    return render(request, 'Articles_app/article_create.html', {'form': form})




def article_list(request):
    if request.user.is_authenticated:
        articles = Article.objects.filter(
            Q(status='published') | Q(author=request.user)
        ).order_by('-created_at')
    else:
        articles = Article.objects.filter(
            status='published'
        ).order_by('-created_at')
    return render(request, 'Articles_app/rule.html', {'articles': articles})



@login_required
def article_publish(request, pk):
    article = get_object_or_404(Article, pk=pk, author=request.user)
    article.status = 'published'
    article.save()
    return redirect('articles')


@login_required
def article_edit(request, pk):
    article = get_object_or_404(Article, pk=pk)

    # Автор або група Administrator можуть редагувати
    if not (request.user == article.author or request.user.groups.filter(name='Administrator').exists()):
        return redirect('articles')  # або HttpResponseForbidden()

    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('articles')
    else:
        form = ArticleForm(instance=article)

    return render(request, 'Articles_app/article_edit.html', {'form': form})


@login_required
def article_delete(request, pk):
    article = get_object_or_404(Article, pk=pk)

    # Автор або група Administrator можуть видаляти
    if not (request.user == article.author or request.user.groups.filter(name='Administrator').exists()):
        return redirect('articles')  # або HttpResponseForbidden()

    if request.method == 'POST':
        article.delete()
        return redirect('articles')

    return render(request, 'Articles_app/article_delete.html', {'article': article})




def toggle_like(request, pk):
    article = get_object_or_404(Article, pk=pk)

    if request.user in article.likes.all():
        article.likes.remove(request.user)
        liked = False
    else:
        article.likes.add(request.user)
        liked = True

    return JsonResponse({
        'liked': liked,
        'total_likes': article.likes.count()
    })



