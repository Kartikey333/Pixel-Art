# import modules
import numpy as np
import pandas as pd
import os
import cv2
import matplotlib.pyplot as plt
from PIL import Image
import random

print(f'Pixel Model is Running....')
# --------------------- Preparing base image ------------------#

# Replicating pixel: Making of Base Image
def replicatingPixel(img):
    
    # Assuming img input have nxnx3 dimension ie. same width and hight
    img_size = img.shape[0]
    enlar_size = img_size*img_size
    
    enlar = np.empty([img_size*img_size,img_size*img_size,3],dtype = np.uint8,order = 'C')
    
    for i in range(enlar_size):
        for j in range(enlar_size):
            
            x = i // img_size
            y = j // img_size
            enlar[i][j] = img[x][y]
            
    return enlar

# Base image
# img = '.\pixel_cat_images\pexels-pixabay-45170.jpg'
# img = cv2.imread(img)
# img = cv2.resize(img,(100,100))
# print(f'Base Image initial size: {img.shape}')
# plt.imshow(cv2.cvtColor(img,cv2.COLOR_BGR2RGB))
# plt.show()

# Replicating pixel -- Now (100x100) = (10000x10000) image size

# base_enlar_img = replicatingPixel(img)
# print(f'Base Image after enlarging size: {base_enlar_img.shape}')
# plt.imshow(cv2.cvtColor(base_enlar_img,cv2.COLOR_BGR2RGB))
# plt.show()

#-----------------------Preparing filler images ------------------------#

class ImageIterator:
    def __init__(self, folder_path):
        # Initialize with the path to the folder and list the image files
        self.folder_path = folder_path
        self.image_files = [f for f in os.listdir(folder_path) if f.endswith(('.png', '.jpg', '.jpeg'))]
        self.index = 0  # Start index for images

    def __iter__(self):
        # Return the iterator object itself
        return self

    def __next__(self):
        # Return the next image or raise StopIteration
        if self.index < len(self.image_files):
            image_file = self.image_files[self.index]
            self.index += 1
            image_path = os.path.join(self.folder_path, image_file)
            img = cv2.imread(image_path)

            if img is None:
                print(f"Error loading image: {image_file}")
                return self.__next__()  # Skip to the next image if loading fails
            
            return img
        else:
            raise StopIteration  # No more images


# Preprocessing function for all image
def preprocess(img, resize_to):
    size = resize_to
    if img is None:
        print("Error: Could not load the image. Please check the file path.")
    else:
        new_img = cv2.resize(img,(size, size))
        return new_img

# Making image pool ready!
def ImagePoolRefurnish(folder_path, pixels):

    imagePool = []
    for file in os.listdir(folder_path):
        imagePool.append(file)
    random.shuffle(imagePool)
    
    n = pixels #Base image dimension -- n x n --pixels
    imagesReq = n * n #image_required_to_make_whole_image
    
    poolImagesLen = len(imagePool)
    print(f'Images in pool :{poolImagesLen}')
    if poolImagesLen < imagesReq:
        more_needed = imagesReq // poolImagesLen
        imagePool = imagePool *  (more_needed + 1)
        print(f'Now images in pool :{len(imagePool)}')
        random.shuffle(imagePool)

        
    random.shuffle(imagePool)
    random.shuffle(imagePool)

    return imagePool
            

class Filler:
    def __init__(self, size, folder_path, image_pool):
        self.size = size
        self.folder_path = folder_path
        self.image_iterator = ImageIterator(folder_path) # initializing image iterator
        self.cnt = 0
        self.data = image_pool

    def rowCreation(self, cnt):
        row = []
        i = 0
        while i < self.size-1:
            image_name = self.data[cnt]
            full_path = os.path.join(self.folder_path, image_name)

            baseimg = cv2.imread(full_path)
            
            baseimg = preprocess(baseimg, self.size)
                                                    
            if len(row) == 0:
                row = baseimg
                continue
            row = np.hstack((row,baseimg))
            print(f'    Image no: {i}')
            i += 1
            cnt += 1
        return row,cnt

    def buildingRowOverRow(self, cnt):
        img = []
        i = 0
        while i < self.size-1:
            baserow,cnt = self.rowCreation(cnt)
            cnt += 1
            if len(img) == 0:
                img = baserow
                continue
            img = np.vstack((img,baserow))
            print(f'Row complete: {i}')
            i += 1
        return img



folder_path = '.\pixel_cat_images'  

pixels = 50
# image_pool = ImagePoolRefurnish(folder_path, pixels)
# filler = Filler(pixels, folder_path, image_pool)

# image = filler.buildingRowOverRow(0)

# print(f'Base Image initial size: {image.shape}')
# plt.imshow(cv2.cvtColor(image,cv2.COLOR_BGR2RGB))
# plt.show()






# import random
# def generateRow(n,data,cnt):
#     row = []
#     i = 0
#     while i < n-1:
#         baseimg = cv2.imread('./family_images/' + data[cnt])
        
#         baseimg = preprocess(baseimg, 100)
                                                 
#         if len(row) == 0:
#             row = baseimg
#             continue
#         row = np.hstack((row,baseimg))
#         i += 1
#         cnt += 1
#     return row,cnt

# # Adding rows vertically to generate a img
# def generateimg(n,data,cnt):
#     col = []
#     i = 0
#     while i < n-1:
#         baserow,cnt = generateRow(n,data,cnt)
#         cnt += 1
#         if len(col) == 0:
#             col = baserow
#             continue
#         col = np.vstack((col,baserow))
#         i += 1
#     return col

# # Function to generate unique images
# def getUniqueImage():

#     data = []
#     for file in os.listdir('./project_images'):
#         data.append(file)
    
#     random.shuffle(data)
# #     sam_img = './family_images/' + data[0] 
# #     sam_img = cv2.imread(sam_img)
# #     re_img = cv2.resize(sam_img,(50,50))

#     # n  --> Transparent image dimension -- n x n 
#     # m --> Images used to replace pixels -- m x m
    
#     # How many images required of 200 x 200 dimension to cover (100x100) -> 10000 one row == 10000 / 200 = 50
    
#     n = 100
    
#     m = image_required_to_make_whole_image = n * n
    
#     while len(data) <= m:
#         base = data
#         data.extend(base)
        
#     random.shuffle(data)
#     random.shuffle(data)
        
#     print(len(data))
    
#     cnt = 0   
#     img = generateimg(n,data,cnt)
    
#     return img