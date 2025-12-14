from django.shortcuts import render
from Articles_app.models import Article
from Categorys_app.models import Category

def home(request):
    latest_articles = Article.objects.filter(status="published").order_by('-created_at')[:5]
    categories = Category.objects.all()
    popular = Article.objects.filter(status="published").order_by('-created_at')[:3]

    return render(request, 'blog/home.html', {
        "latest_articles": latest_articles,
        "categories": categories,
        "popular": popular,
    })
