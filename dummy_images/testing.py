import os

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
last_image = get_last_image_in_folder(folder_path)
print(last_image)

import cv2
import matplotlib.pyplot as plt 

img = cv2.imread(last_image)
plt.imshow(img)
plt.show()
