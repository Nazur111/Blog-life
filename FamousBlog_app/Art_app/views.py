from django.shortcuts import render

def index(request):
    return render(request, "Art_app/paint.html")