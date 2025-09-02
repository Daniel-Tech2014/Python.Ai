import cv2
#Load the Image#
image = cv2.imread('Lena.png')
#Resize the window to a specific size
cv2.namedWindow( 'Loaded Image', cv2.WINDOW_NORMAL)
cv2.resizeWindow( 'Loaded Image', 800, 500)
cv2.imshow('Loaded Image', image)
cv2.waitkey(0)
cv2.destroyAllWindows()
print(f"Image Dimensions: {image.shape}") 
