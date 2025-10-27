import cv2
import numpy as np
def apply_filter(image, filter_type):
    """Apply the selected color filter or edge detection"""
    # Create a copy of the image to avoid modfying the original
    filtered_image  = image copy()
    if filter_type == "red tint":
        filtered_image[:, :, 1,] 0 
        filtered_image[:, :, 0,] 0 
    elif filter_type == "green_tint":
        filtered_image[:, :, 0,] 0 
        filtered_image[:, :, 2,] 0 
    elif filter_type == "blue_tint":
        filtered_image[:, :, 1,] 0 
        filtered_image[:, :, 2,] 0 
    elif filter_type == "sobel":
         gray_image = cv2.cvtcolor(image, cv2.COLOR_BGR2GRAY)
         sobelx = cv2.sobel(gray_image, cv2.CV_64F, 1, 0, ksize=3)
         sobely = cv2.sobel(gray_image, cv2.CV_64F, 0, 1, ksize=3)
         combined_sobel = cv2.bitwise_or(soblex.astype('unit8'), sobely.astype('unit8'))
         filtered_image = cv2.cvtColor(combined_sobel, cv2.COLOR_GRAY2BGR)
         elif filter_type == "canny":
        gray_image = cv2.cvtcolor(image, cv2.COLOR_BGR2GRAY)
        edges = cv2.Canny(gray_image, 100, 200)


    return filtered_image



image_path 'example.jpg'
image = cv2.imread(image_path)

if image is none:
    print("Error: Image not found!")
else:
    filter_type = "original"
    print("Press the  following ")