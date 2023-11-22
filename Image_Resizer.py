import cv2
import matplotlib.pyplot as plt

image = cv2.imread("_path_")
plt.imshow(image)

#? Code for resizing the image
scale_percent=50
width = int(image.shape[1]*scale_percent / 100)
height = int(image.shape[0]*scale_percent / 100)

dsize = (width, height)
output = cv2.resize(image, dsize=dsize)
plt.imshow(output)
cv2.waitKey(0)