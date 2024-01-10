import cv2
import numpy as np

img = cv2.imread("images/cube_1.jpg")
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
lower_yellow = np.array([23, 104, 123])
upper_yellow = np.array([40, 255, 255])
mask = cv2.inRange(hsv, lower_yellow, upper_yellow)

# Resize the image and the mask to 800 x 600
img = cv2.resize(img, (800, 600))
mask = cv2.resize(mask, (800, 600))

# Find the contours of the yellow region in the mask
contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

if contours:
    # Get the largest contour, assuming it is the cube
    cnt = max(contours, key=cv2.contourArea)

    # Get the x, y coordinates of the top-left corner of the bounding box, and its length and width
    x, y, l, w = cv2.boundingRect(cnt)

    # Draw the bounding box on the original image
    cv2.rectangle(img, (x, y), (x + l, y + w), (0, 255, 0), 2)

    # Get the pixel per cm ratio of the image using the dpi value and the conversion factor of 2.54
    dpi = 96  # Based on pixel density of image
    pcm = dpi / 2.54

    # Convert the x, y, w, h values to centimeters by dividing them by pcm ratio
    x_cm = x / pcm
    y_cm = y / pcm
    l_cm = l / pcm
    w_cm = w / pcm

    print(f"Coordinates: ({x}, {y}) in pixels")  # x from the left, y from the top
    print(f"Length: {l} in pixels")
    print(f"Width: {w} in pixels")

    print(f"Coordinates: ({x_cm:.2f}, {y_cm:.2f}) cm")
    print(f"Length: {l_cm:.2f} cm")
    print(f"Width: {w_cm:.2f} cm")
    print(f"Actual Length: 7 cm")
    print(f"Actual Width: 7 cm")
else:
    print("No contours found.")

cv2.namedWindow("Original", cv2.WINDOW_NORMAL)
cv2.namedWindow("Mask", cv2.WINDOW_NORMAL)
cv2.imshow("Original", img)
cv2.imshow("Mask", mask)
cv2.waitKey(0)
cv2.destroyAllWindows()
