from django.shortcuts import render, redirect, get_object_or_404
from .models import Category

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'categories/list.html', {"categories": categories})

def category_create(request):
    if request.method == "POST":
        Category.objects.create(name=request.POST['name'])
        return redirect('category_list')
    return render(request, 'categories/create.html')

def category_delete(request, pk):
    cat = get_object_or_404(Category, pk=pk)
    cat.delete()
    return redirect('category_list')

