import cv2
import matplotlib.pyplot as plt
image = cv2.imread(example.jpg)
# Convert BGR to RBG
image_rbg = cv2.cvtColor(image, cv2.COLOR_BGR2RBG)
plt.imshow(image_rbg)
plt.title("RBG Image")
plt.show()
#Convert to GrayScale
grey_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
plt.imshow(grey_image, cmap='gray')
plt.title("GrayScale Image")
plt.show()
#Cropping the image
#Assume we know the region we want: rows 100 to 300, colums 200 to 400
cropped_image = image[100:300, 200:400]
cropped_rgb = cv2.cvtColor(cropped_image, cv2.COLOR_BGR2RBG)
plt.imshow(cropped_rgb)
plt.title("Cropped Region")
plt.show()


