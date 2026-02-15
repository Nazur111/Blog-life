from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import AdvertisementForm
from .models import Advertisement

def head_page(request):
    adverts = Advertisement.objects.all().order_by('-created_at')  # останні зверху
    return render(request, 'Advertisement_app/head.html', {'adverts': adverts})


@login_required
def advert_create(request):
    if request.method == 'POST':
        form = AdvertisementForm(request.POST)
        if form.is_valid():
            advert = form.save(commit=False)  
            advert.author = request.user      
            advert.save()                     
            return redirect('head')
    else:
        form = AdvertisementForm()
    return render(request, 'Advertisement_app/advert_create.html', {'form': form})


def advert_delete(request, pk):
    advert = get_object_or_404(Advertisement, pk=pk)

    if advert.author != request.user:
        return redirect('head')

    if request.method == 'POST':
        advert.delete()
        return redirect('head')

    return render(
        request,
        'Advertisement_app/advert_delete.html',
        {'advert': advert}
    )



def advert_edit(request, pk):
    advert = get_object_or_404(Advertisement, pk=pk)

    if advert.author != request.user:
        return redirect('head')

    if request.method == 'POST':
        form = AdvertisementForm(request.POST, instance=advert)
        if form.is_valid():
            form.save()
            return redirect('head')
    else:
        form = AdvertisementForm(instance=advert)

    return render(request, 'Advertisement_app/advert_edit.html', {'form': form})




