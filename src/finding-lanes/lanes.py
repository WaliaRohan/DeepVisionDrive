import cv2
import os

absolute_path = os.path.join(os.getcwd(), "files", "test_image.jpg") # os.getcwd() = project root folder
image = cv2.imread(absolute_path)
cv2.imshow('result', image)
cv2.waitKey(0)