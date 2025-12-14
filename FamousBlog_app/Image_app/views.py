from django.shortcuts import render, redirect
from .models import ImageFile

def image_upload(request):
    if request.method == "POST" and request.FILES.get('file'):
        ImageFile.objects.create(file=request.FILES['file'])
        return redirect('image_list')
    return render(request, 'images/upload.html')

def image_list(request):
    images = ImageFile.objects.all()
    return render(request, 'images/list.html', {"images": images})
