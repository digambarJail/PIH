from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Image
from django.shortcuts import render, redirect, get_object_or_404
from .forms import ImageForm



def image_gallery(request):
    image_list = Image.objects.all()
    paginator = Paginator(image_list, 10)  # Show 10 images per page

    page = request.GET.get('page')
    try:
        images = paginator.page(page)
    except PageNotAnInteger:
        # If the page parameter is not an integer, go to the first page
        images = paginator.page(1)
    except EmptyPage:
        # If the page is out of range, deliver the last page of results
        images = paginator.page(paginator.num_pages)

    return render(request, 'gallery.html', {'images': images})

def image_upload(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('gallery')
    else:
        form = ImageForm()
    return render(request, 'upload.html', {'form': form})


def image_lightbox(request, image_id):
    image = get_object_or_404(Image, pk=image_id)
    return render(request, 'lightbox.html', {'image': image})



