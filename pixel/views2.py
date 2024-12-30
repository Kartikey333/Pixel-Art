# views.py
from django.shortcuts import render, redirect
from pixel.models import Photo

# Define the fixed folders
FOLDER_1 = 'static/folder1'
FOLDER_2 = 'static/folder2'
FOLDER_3 = 'static/folder3'
FOLDER_4 = 'static/folder4'

def main_create(request, pk=None):
    if request.method == 'POST':
        data = request.POST
        image = request.FILES.get('image')

        photo = Photo.objects.create(
            description=data['description'],
            image=image,
            upload_folder=FOLDER_1  # Use the appropriate folder
        )

        return redirect('main_create_with_pk', pk=photo.pk)

    photo = None
    if pk:
        try:
            photo = Photo.objects.get(id=pk)
        except Photo.DoesNotExist:
            photo = None
    return render(request, 'main_create.html', {'photo': photo})

def create(request):
    if request.method == 'POST':
        data = request.POST
        images = request.FILES.getlist('images')

        for image in images:
            photo = Photo.objects.create(
                description=data['description'],
                image=image,
                upload_folder=FOLDER_2  # Use the appropriate folder
            )

    photos = Photo.objects.all()
    context = {'photos': photos}
    return render(request, 'create.html', context)

# You can define other views and assign FOLDER_3, FOLDER_4 as needed
