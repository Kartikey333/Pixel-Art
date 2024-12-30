from django.shortcuts import render, redirect

import numpy as np
from PIL import Image
import cv2
import io
import os
import sys
from django.core.files.base import ContentFile

import json
from subprocess import run, PIPE
import subprocess
from django.http import HttpResponse
from pixel.models import Photo
from pixel.scripts import script1
from django.core.files import File


# Define the fixed folders
FOLDER_base = 'base/'
FOLDER_all_images = 'images/'
FOLDER_creation = 'creation/'
FOLDER_filler_get_together = 'Filler_together/'


def index(request):
    out = run([sys.executable,'pixel\pixel_model_final.py'], stdout= PIPE)
    return render(request, 'result.html', {'photo':out})


def run_script_view(request):
    # Retrieve Photo objects or use them as input to your script
    photos = Photo.objects.all()

    # Run the script and get the output (modify this to suit your script's needs)
    script_output = script1.main()

    # Pass the script output to the template
    context = {
        'script_output': script_output,
        'photos': photos,
    }
    return render(request, 'result.html', context)

def home(request):
    return render(request, 'home.html')


def viewPhoto(request, pk):
    photo = Photo.objects.get(id=pk)
    return render(request, 'photo.html', {'photo': photo})

def main_create(request, pk=None):
    
    photo = None
    base_img_id = None
    if request.method == 'POST':
        data = request.POST
        image = request.FILES.get('image')
        
        print(data, " ", image)
        photo = Photo.objects.create(
            description=data['description'],
            image=image,
            upload_folder = FOLDER_base
        )
        base_img = photo

        return redirect('main_create_with_pk', pk=photo.pk)

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
                upload_folder = FOLDER_all_images
            )
            
    photos = Photo.objects.filter(upload_folder=FOLDER_all_images)
    All_fillers = photos
    context = {'photos': photos}
    return render(request, 'create.html', context)

def get_last_image_in_folder(folder_path):
    # List all files in the folder
    files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
    
    # Filter for image files (optional, based on file extensions)
    image_files = [f for f in files if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp', '.tiff'))]
    
    # Sort files by modification time (newest first)
    image_files.sort(key=lambda x: os.path.getmtime(os.path.join(folder_path, x)), reverse=True)

    # Return the last entered (newest) image file
    if image_files:
        return os.path.join(folder_path, image_files[0])
    else:
        return None

# Example usage
folder_path = './static/creation/'  # Replace with your folder path
last_img_path = get_last_image_in_folder(folder_path)
print(last_img_path)

def run_model(request):
    # Run a script or file (for example, a Python script)
    # Using subprocess to run a Python script or any other file

    unique_name = request.POST.get('name') 

    python_executable = 'D:\Django_Projects\PixelArt\pixelWorld\Scripts\python.exe'
    script_path = os.path.join(os.path.dirname(__file__), 'pixel_model_final.py')

    if not os.path.exists(script_path):
        return HttpResponse(f"Script file not found: {script_path}")
        
    if os.path.exists(last_img_path):
            # Open the image file
        with open(last_img_path, 'rb') as img_file:
            photo = Photo.objects.create(
                description=unique_name,
                image=File(img_file),  # Pass the file object to the image field
                upload_folder='FOLDER_creation'  # Adjust as needed
            )
    # Run the Python script
    result = subprocess.run([python_executable, script_path, unique_name], capture_output=True, text=True)
    
    # return_data = json.loads(result.stdout)

    output = result.stdout
    error = result.stderr

    # print(" Output is {}".format(output))
    img = photo

    # img_data  = json.loads(output)

    # img_array = np.array(img_data, dtype= np.uint8)
    # img = Image.fromarray(img_array)

    #     # Save the image to a BytesIO object
    # img_io = io.BytesIO()
    # img.save(img_io, format='PNG')  # You can choose 'JPEG' or any format supported by PIL
    # img_io.seek(0)

        # Create a new Photo instance
    # name_input = name_input # Replace this with your actual description
    # photo = Photo.objects.create(
    #     description=name_input,
    #     image=ContentFile(img_io.read(), name='image.png')  # Create a ContentFile
    #     )
    # Check if the process was successful
    # dtype = int(img_data)

    if result.returncode == 0:
        context = {'photo': img, 'dtype': 0}
        return render(request, 'result.html', context)
    else:
        return HttpResponse(f"Script failed with error: {error}")
