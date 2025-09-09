import cv2
import matplotlib.pylot as plt
# Step 1 : Load the image
image_path = 'example.jpg'   #User provided image path
image = cv2.imread(image_path)
# BGR to RGB for correct colour display with matplotlib
image_rbg = cv2.cvtColor(image, cv2.COLOR_BGR2RBG)
 # Get image dimensions
 height, width,_ = image_rbg.shape

# Step 2 : Draw 2 rectangles Around Interesting Regions
# Rectangle 1: Top-left Corner
rectl_width, rectl_height = 150, 150
top_left1 = (20, 20) # Fixed 20 pixels padding from top-left
bottom_right1 = (top_left1[0] + rectl_width, top_left1[ 1 ] + rectl_height)
cv2.rectangle(image_rgb, top_left1, bottom_right1, (0, 255, 255), 3) # Yellow rectangle

#Rectangle 2: Bottom-right Corner
rect2_width, rect2_height = 200, 150
top_left2 = (width - rect2_width - 20, height - rect2_height - 20)  # 20pixels padding
bottom_right2 = (top_left2[0] + rect2_width, top_left2[1] + rect2_height)
cv2.rectangle(image_rgb, top_left2, bottom_right2 , (255, 0, 255), 3) # Magenta rectangle

# Step 3 : Draw Circles at the centers of both rectangles
center1_x = top_left1[0] + rectl_width // 2
center1_x = top_left1[1] + rectl_width // 2
center1_x = top_left1[0] + rectl_width // 2
center1_x = top_left1[1] + rectl_width // 2
cv2.circle(image_rgb, (Center1_x, center1_y ), (0, 255, 0), -1) # Filled green circle
cv2.circle(image_rgb, (Center2_x, center2_y ), (0, 0, 255), -1) # Filled red circle


