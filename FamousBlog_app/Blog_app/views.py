
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from FamousBlog_app.Articles_app.models import Article

def home(request):
    return render(request, 'Blog/home.html', {
    'articles': Article.objects.filter(status='published')
})



@login_required
def toggle_like(request, pk):
    article = get_object_or_404(Article, pk=pk)

    if request.user in article.likes.all():
        article.likes.remove(request.user)
    else:
        article.likes.add(request.user)

    return redirect(request.META.get("HTTP_REFERER", "/"))
