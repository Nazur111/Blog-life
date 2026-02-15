from django.shortcuts import render

def index(request):
    return render(request, 'Image_app/index.html')
